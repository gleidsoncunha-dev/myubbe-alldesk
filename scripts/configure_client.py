"""Configure only the server options of a stopped MyUbbe AllDesk client."""
import datetime
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tomllib


def main():
    root = Path(__file__).resolve().parents[1]
    profile = json.loads((root / 'deploy/client-config.json').read_text())
    if sys.platform == 'win32':
        processes = subprocess.check_output(['tasklist', '/FI', 'IMAGENAME eq MyUbbeAllDesk.exe', '/FO', 'CSV'], text=True)
        running = 'myubbealldesk.exe' in processes.lower()
        folder = Path(os.environ['APPDATA']) / 'MyUbbeAllDesk' / 'config'
    elif sys.platform == 'darwin':
        running = subprocess.run(['pgrep', '-x', 'MyUbbeAllDesk'], stdout=subprocess.DEVNULL).returncode == 0
        folder = Path.home() / 'Library' / 'Preferences' / 'com.carriez.MyUbbeAllDesk'
    else:
        raise SystemExit('Use Windows ou macOS.')
    if running:
        raise SystemExit('Encerre o MyUbbe AllDesk antes de aplicar a configuracao.')
    target = folder / 'MyUbbeAllDesk2.toml'
    if not target.is_file():
        raise SystemExit(f'Configuracao nao encontrada: {target}. Abra e encerre o aplicativo primeiro.')
    original = target.read_text(encoding='utf-8')
    parsed = tomllib.loads(original)
    replacements = {'custom-rendezvous-server': profile['host'], 'relay-server': profile['relay'], 'key': profile['key']}
    text = original
    if not re.search(r'^\[options\]\s*$', text, re.M):
        text += '\n[options]\n'
    section = re.search(r'^\[options\]\s*\n(.*?)(?=^\[|\Z)', text, re.M | re.S)
    content = section[1]
    for key, value in replacements.items():
        line = f'{key} = {json.dumps(value)}'
        pattern = rf'^{re.escape(key)}\s*=.*$'
        if re.search(pattern, content, re.M):
            content = re.sub(pattern, lambda _: line, content, flags=re.M)
        else:
            content += '\n' + line + '\n'
    text = text[:section.start(1)] + content + text[section.end(1):]
    updated = tomllib.loads(text)
    expected = dict(parsed.get('options', {})) | replacements
    assert updated.get('options') == expected
    assert {k: v for k, v in parsed.items() if k != 'options'} == {k: v for k, v in updated.items() if k != 'options'}
    stamp = datetime.datetime.now().strftime('%Y%m%dT%H%M%S%f')
    backup = target.with_suffix(f'.toml.before-myubbe-vps-{stamp}')
    shutil.copy2(target, backup)
    temporary = target.with_suffix('.toml.tmp')
    temporary.write_text(text, encoding='utf-8')
    temporary.replace(target)
    print('Servidor configurado. Backup preservado. Abra o MyUbbe AllDesk.')


if __name__ == '__main__':
    main()
