#!/usr/bin/env python3
"""Package one skill directory as a Claude-compatible .skill archive."""

from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

IGNORED_NAMES = {".DS_Store", "__pycache__"}


def package_skill(skill_directory: Path, output_directory: Path) -> Path:
    """Validate and package a skill directory."""
    skill_directory = skill_directory.resolve()
    if not skill_directory.is_dir():
        raise ValueError(f"Skill directory not found: {skill_directory}")
    if not (skill_directory / "SKILL.md").is_file():
        raise ValueError(f"SKILL.md not found in: {skill_directory}")

    output_directory.mkdir(parents=True, exist_ok=True)
    output_path = output_directory.resolve() / f"{skill_directory.name}.skill"

    files = [
        path
        for path in skill_directory.rglob("*")
        if path.is_file()
        and not path.is_symlink()
        and not any(part in IGNORED_NAMES for part in path.parts)
        and path.suffix != ".pyc"
    ]
    if not files:
        raise ValueError(f"No packageable files found in: {skill_directory}")

    with ZipFile(output_path, "w", ZIP_DEFLATED) as archive:
        for path in sorted(files):
            archive.write(
                path, Path(skill_directory.name) / path.relative_to(skill_directory)
            )

    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_directory", type=Path)
    parser.add_argument("--output-directory", type=Path, default=Path("dist"))
    arguments = parser.parse_args()

    output_path = package_skill(arguments.skill_directory, arguments.output_directory)
    print(output_path)


if __name__ == "__main__":
    main()
