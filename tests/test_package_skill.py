from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from zipfile import ZipFile

from scripts.package_skill import package_skill


class PackageSkillTest(TestCase):
    def test_packages_skill_with_root_directory(self) -> None:
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            skill = root / "example-skill"
            (skill / "references").mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: example-skill\n---\n")
            (skill / "references" / "guide.md").write_text("# Guide\n")
            (skill / ".DS_Store").write_text("ignored")
            (skill / "outside-link").symlink_to(root / "outside.txt")
            (root / "outside.txt").write_text("must not be packaged")

            output = package_skill(skill, root / "dist")

            with ZipFile(output) as archive:
                self.assertEqual(
                    archive.namelist(),
                    [
                        "example-skill/SKILL.md",
                        "example-skill/references/guide.md",
                    ],
                )

    def test_rejects_directory_without_skill_manifest(self) -> None:
        with TemporaryDirectory() as temporary_directory:
            skill = Path(temporary_directory) / "invalid"
            skill.mkdir()

            with self.assertRaisesRegex(ValueError, "SKILL.md not found"):
                package_skill(skill, Path(temporary_directory) / "dist")
