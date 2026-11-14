#!/usr/bin/env bash
set -euo pipefail
umask 077
cd "$(dirname "$0")/../.."
root=/opt/myubbe-alldesk
release=$(python3 -c 'import tomllib; print(tomllib.load(open("Cargo.toml","rb"))["package"]["version"])')
test "$(realpath .)" = "$root/releases/$release"
test -s "$root/shared/data/id_ed25519"
python3 - <<'PY'
import json
from pathlib import Path
profile = json.loads(Path('deploy/client-config.json').read_text())
assert Path('/opt/myubbe-alldesk/shared/data/id_ed25519.pub').read_text().strip() == profile['key'], 'Server key differs from clients'
PY
chmod 700 "$root/shared" "$root/shared/data"
chmod 600 "$root/shared/data/id_ed25519"
install -d -m 700 "$root/shared/backups"
# A consistent SQLite backup and the original keys stay on the VPS.
python3 - <<'PY'
import datetime, shutil, sqlite3
from pathlib import Path
data = Path('/opt/myubbe-alldesk/shared/data')
backup = data.parent / 'backups' / datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
backup.mkdir(mode=0o700)
for name in ('id_ed25519', 'id_ed25519.pub'):
    shutil.copy2(data / name, backup / name)
if (data / 'db_v2.sqlite3').exists():
    with sqlite3.connect(data / 'db_v2.sqlite3') as source, sqlite3.connect(backup / 'db_v2.sqlite3') as target:
        source.backup(target)
PY
docker compose -f deploy/vps/compose.yaml config --quiet
docker compose -f deploy/vps/compose.yaml pull
docker compose -f deploy/vps/compose.yaml up -d --wait --wait-timeout 120
python3 scripts/check_server.py --host 127.0.0.1
ln -sfn "$root/releases/$release" "$root/current"
printf 'PUBLICACAO_VERIFICADA MyUbbeAllDesk %s\n' "$release"
