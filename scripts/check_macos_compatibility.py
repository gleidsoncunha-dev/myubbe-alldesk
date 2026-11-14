"""Check deployment metadata in the built app and its bundled Mach-O files."""

import argparse
import plistlib
import re
import subprocess
from pathlib import Path


def version(value):
    if not re.fullmatch(r"\d+(?:\.\d+){0,2}", value):
        raise ValueError(f"Invalid macOS version: {value}")
    parts = tuple(int(part) for part in value.split("."))
    return parts + (0,) * (3 - len(parts))


def check_bundle(app, architecture, maximum):
    limit = version(maximum)
    with (app / "Contents/Info.plist").open("rb") as source:
        info = plistlib.load(source)
    if version(info["LSMinimumSystemVersion"]) > limit:
        raise ValueError(f"Bundle requires macOS {info['LSMinimumSystemVersion']}")

    arch = {"x86_64": "x86_64", "aarch64": "arm64"}[architecture]
    magic = {bytes.fromhex(value) for value in (
        "feedface", "cefaedfe", "feedfacf", "cffaedfe",
        "cafebabe", "bebafeca", "cafebabf", "bfbafeca",
    )}
    checked = 0
    for path in sorted(app.rglob("*")):
        if path.is_symlink() or not path.is_file():
            continue
        with path.open("rb") as source:
            if source.read(4) not in magic:
                continue
        subprocess.run(["xcrun", "lipo", str(path), "-verify_arch", arch], check=True)
        report = subprocess.check_output(
            ["xcrun", "vtool", "-show-build", "-arch", arch, str(path)], text=True)
        minimums = re.findall(r"^\s*minos\s+([\d.]+)\s*$", report, re.M)
        if not minimums and "LC_VERSION_MIN_MACOSX" in report:
            minimums = re.findall(r"^\s*version\s+([\d.]+)\s*$", report, re.M)
        for minimum in minimums:
            if version(minimum) > limit:
                raise ValueError(f"{path.relative_to(app)} requires macOS {minimum}")
        checked += 1
        print(f"{path.relative_to(app)}: {', '.join(minimums) or 'no explicit minimum'}")
    if not checked:
        raise ValueError("No Mach-O binaries found in app bundle")
    print(f"Checked {checked} {arch} binaries: no declared minimum exceeds macOS {maximum}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("app", type=Path)
    parser.add_argument("--architecture", choices=("x86_64", "aarch64"), required=True)
    parser.add_argument("--maximum-macos", required=True)
    args = parser.parse_args()
    check_bundle(args.app, args.architecture, args.maximum_macos)
