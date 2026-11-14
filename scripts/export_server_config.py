"""Export the public server profile in RustDesk's existing import format."""
import base64
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
profile = json.loads((root / 'deploy/client-config.json').read_text())
encoded = base64.urlsafe_b64encode(json.dumps(profile, separators=(',', ':')).encode()).decode().rstrip('=')[::-1]
print(encoded)
