import argparse, json, os, subprocess, sys, textwrap
from dataclasses import dataclass, asdict
from pathlib import Path

def main():
    if os.geteuid() != 0:
        sys.exit("Run as root.")

    ap = argparse.ArgumentParser(description="archinstall-style installer for NixOS (skeleton)")
    ap.add_argument("--config", help="JSON file to load/save configuration")
    ap.add_argument("--dump-example", action="store_true", help="Print example JSON and exit")
    args = ap.parse_args()

    if args.dump_example:
        example = InstallConfig(users=[UserConfig("alice", "hunter2")])
        print(json.dumps(asdict(example), indent=2))
        return
