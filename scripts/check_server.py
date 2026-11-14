"""Read-only TCP probes for the native AllDesk server."""
import argparse
import json
import socket


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host', default='195.182.200.177')
    args = parser.parse_args()
    results = {}
    for port in (21115, 21116, 21117):
        with socket.create_connection((args.host, port), timeout=8):
            results[str(port)] = 'reachable'
    print(json.dumps({'host': args.host, 'tcp': results}, sort_keys=True))


if __name__ == '__main__':
    main()
