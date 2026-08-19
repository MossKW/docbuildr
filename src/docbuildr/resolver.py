from __future__ import annotations

from pathlib import PurePosixPath

import requests


class AssetResolver:
    """Resolve relative image URLs."""

    def __init__(self):

        self.cache: dict[str, str] = {}

        self.session = requests.Session()

    def resolve(
        self,
        markdown_path: str,
        asset: str,
    ) -> str:

        if asset.startswith("http"):
            return asset

        asset = asset.strip()

        asset = asset.lstrip("./")

        key = markdown_path + "|" + asset

        if key in self.cache:
            return self.cache[key]

        folder = PurePosixPath(markdown_path).parent

        candidates = [

            # same folder in GitHub repository
            (
                "https://raw.githubusercontent.com/"
                "gtonkinhill/panaroo/master/docs/"
                f"{folder}/{asset}"
            ),

            # docs root
            (
                "https://raw.githubusercontent.com/"
                "gtonkinhill/panaroo/master/docs/"
                f"{asset}"
            ),

            # same folder on website
            (
                "https://gthlab.au/panaroo/"
                f"{folder}/{asset}"
            ),

            # website root
            (
                "https://gthlab.au/panaroo/"
                f"{asset}"
            ),

        ]

        for url in candidates:

            try:

                r = self.session.head(
                    url,
                    timeout=5,
                    allow_redirects=True,
                )

                if r.status_code == 200:

                    self.cache[key] = url

                    return url

            except requests.RequestException:
                pass

        self.cache[key] = candidates[-1]

        return candidates[-1]
