from __future__ import annotations

from pathlib import Path
import shutil


class AssetManager:
    """Copy static assets into the output directory."""

    def copy_assets(
        self,
        output_dir: Path,
    ) -> None:

        self._copy_directory(
            Path("templates/styles"),
            output_dir / "styles",
        )

        self._copy_directory(
            Path("templates/vendor"),
            output_dir / "vendor",
        )

    def _copy_directory(
        self,
        source: Path,
        destination: Path,
    ) -> None:

        if not source.exists():
            return

        if destination.exists():
            shutil.rmtree(destination)

        shutil.copytree(
            source,
            destination,
        )
