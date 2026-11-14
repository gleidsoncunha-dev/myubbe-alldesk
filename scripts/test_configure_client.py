import os
from pathlib import Path
import tempfile
import tomllib
import unittest
from unittest.mock import patch

import configure_client


class ConfigureClientTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.folder = Path(self.temporary.name) / 'MyUbbeAllDesk' / 'config'
        self.folder.mkdir(parents=True)
        self.target = self.folder / 'MyUbbeAllDesk2.toml'
        self.original = "rendezvous_server = 'old.example:21116'\nnat_type = 1\n[options]\nkey = 'old-key'\nverification-method = 'use-both-passwords'\n[other]\nvalue = 'preserved'\n"
        self.target.write_text(self.original)

    def invoke(self, processes=''):
        with patch.object(configure_client.sys, 'platform', 'win32'), patch.dict(os.environ, {'APPDATA': self.temporary.name}), patch.object(configure_client.subprocess, 'check_output', return_value=processes):
            configure_client.main()

    def test_preserves_other_settings_and_original_backup(self):
        self.invoke()
        actual = tomllib.loads(self.target.read_text())
        self.assertEqual(actual['options']['custom-rendezvous-server'], '195.182.200.177')
        self.assertEqual(actual['options']['verification-method'], 'use-both-passwords')
        self.assertEqual(actual['other']['value'], 'preserved')
        self.assertEqual(actual['nat_type'], 1)
        backups = list(self.folder.glob('*.before-myubbe-vps-*'))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), self.original)

    def test_running_client_is_never_modified(self):
        with self.assertRaises(SystemExit):
            self.invoke('"MyUbbeAllDesk.exe","123"')
        self.assertEqual(self.target.read_text(), self.original)
        self.assertEqual(len(list(self.folder.iterdir())), 1)

    def test_profile_without_options_keeps_identity(self):
        self.target.write_text("rendezvous_server = ''\nnat_type = 0\n")
        self.invoke()
        actual = tomllib.loads(self.target.read_text())
        self.assertEqual(actual['rendezvous_server'], '')
        self.assertEqual(actual['options']['relay-server'], '195.182.200.177')


if __name__ == '__main__':
    unittest.main()
