"""{{ cookiecutter.project_description }}"""

from __future__ import annotations

__all__ = []

import argparse
import os


def main(args: list[str]) -> int:
    """A CLI interface function for {{ cookiecutter.project_name }}."""
    parser = argparse.ArgumentParser("{{ cookiecutter.project_name }}")
    parsed_args = parser.parse_args(args)
    return os.EX_OK
