import argparse, json, os, subprocess, sys, textwrap
from dataclasses import dataclass, asdict
from pathlib import Path

def main():
    if os.geteuid() != 0:
        sys.exit("Run as root.")

