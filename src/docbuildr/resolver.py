from __future__ import annotations

from pathlib import PurePosixPath
from urllib.parse import urljoin


class AssetResolver:
    """Resolve relative asset URLs."""

    def __init__(
        self,
        base_url: str,
    ) -> None:
        self.base_url = base_url.rstrip("/") + "/"

    def resolve(
        self,
        page_path: str,
        asset: str,
    ) -> str:
        asset = asset.strip()

        #
        # Already absolute URL
        #
        if asset.startswith(("http://", "https://")):
            return asset

        #
        # Root-relative asset
        #
        if asset.startswith("/"):
            return urljoin(
                self.base_url,
                asset.lstrip("/"),
            )

        #
        # Relative asset
        #
        folder = PurePosixPath(page_path).parent

        relative = str(folder / asset)

        return urljoin(
            self.base_url,
            relative,
        )
