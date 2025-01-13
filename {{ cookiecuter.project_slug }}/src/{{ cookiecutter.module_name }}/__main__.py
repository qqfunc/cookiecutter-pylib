"""A CLI interface module for {{ cookiecutter.project_name }}."""

from __future__ import annotations

import sys

from . import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
