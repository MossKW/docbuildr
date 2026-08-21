from __future__ import annotations

import shutil
from pathlib import Path
from importlib.resources import files


class AssetManager:
    """Copy bundled static assets into the output directory."""

    def copy_assets(
        self,
        output_dir: Path,
    ) -> None:
        template_root = files("docbuildr").joinpath("templates")

        self._copy_directory(
            Path(str(template_root.joinpath("styles"))),
            output_dir / "styles",
        )

        self._copy_directory(
            Path(str(template_root.joinpath("vendor"))),
            output_dir / "vendor",
        )

    def _copy_directory(
        self,
        source: Path,
        destination: Path,
    ) -> None:
        if destination.exists():
            shutil.rmtree(destination)

        shutil.copytree(
            source,
            destination,
        )
