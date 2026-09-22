"""Runs an example program and saves the string art it draws as an svg file.

Usage:

    python _build.py circle.py circle.svg
"""
import runpy
import sys

import stringart

def main():
    if len(sys.argv) != 3:
        print(__doc__.strip(), file=sys.stderr)
        sys.exit(1)

    src, dest = sys.argv[1:]
    runpy.run_path(src, run_name="__main__")
    stringart.save(dest)

if __name__ == "__main__":
    main()
