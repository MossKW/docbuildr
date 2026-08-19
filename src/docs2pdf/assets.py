from __future__ import annotations

from pathlib import PurePosixPath
from urllib.parse import urlparse


class AssetResolver:
    """Resolve relative asset paths."""

    def resolve(
        self,
        markdown_url: str,
        asset: str,
    ) -> str:

        if asset.startswith("http"):
            return asset

        asset = asset.strip()

        asset = asset.lstrip("./")

        parsed = urlparse(markdown_url)

        path = PurePosixPath(parsed.path)

        folder = path.parent

        return (
            f"https://raw.githubusercontent.com/"
            f"gtonkinhill/panaroo/master/docs/"
            f"{folder.relative_to('/panaroo')}/{asset}"
        )
