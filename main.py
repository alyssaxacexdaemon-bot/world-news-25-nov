#!/usr/bin/env python3
"""Copy the 25 November world-news image into the make.fun output directory.

Standard library only. Reads entry.png next to this file and writes it to
$MAKEFUN_OUTPUT_DIR (default /output) as entry.png, then checks the copy
matches the original. Exits 1 on any failure.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    if not os.path.isfile(SRC):
        print(f"missing: {SRC}", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    if os.path.getsize(SRC) != os.path.getsize(DST):
        print("size mismatch after copy", file=sys.stderr)
        return 1
    with open(SRC, "rb") as f:
        want = hashlib.sha256(f.read()).hexdigest()
    with open(DST, "rb") as f:
        got = hashlib.sha256(f.read()).hexdigest()
    if want != got:
        print("content mismatch after copy", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
