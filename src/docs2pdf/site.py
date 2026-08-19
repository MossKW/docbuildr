from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
import re

import requests


@dataclass(slots=True)
class Page:
    title: str
    path: str
    markdown_url: str


class SiteAdapter(ABC):

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    @abstractmethod
    def pages(self) -> list[Page]:
        ...

    @abstractmethod
    def title(self) -> str:
        ...


class DocsifySite(SiteAdapter):

    def pages(self) -> list[Page]:

        response = requests.get(
            f"{self.base_url}/_sidebar.md",
            timeout=30,
        )
        response.raise_for_status()

        sidebar = response.text

        # Remove HTML comments
        sidebar = re.sub(
            r"<!--.*?-->",
            "",
            sidebar,
            flags=re.DOTALL,
        )

        pages: list[Page] = []

        for title, path in re.findall(
            r"\[(.*?)\]\((.*?)\)",
            sidebar,
        ):

            if path.startswith("http"):
                continue

            clean = path.strip().lstrip("/")

            pages.append(
                Page(
                    title=title,
                    path=clean,
                    markdown_url=f"{self.base_url}/{clean}",
                )
            )

        return pages

    def title(self) -> str:
        """
        Return a human-readable documentation title.
        """

        try:

            response = requests.get(
                self.base_url,
                timeout=15,
            )

            response.raise_for_status()

            html = response.text

            # Try HTML <title>
            match = re.search(
                r"<title>(.*?)</title>",
                html,
                flags=re.IGNORECASE | re.DOTALL,
            )

            if match:

                title = re.sub(
                    r"\s+",
                    " ",
                    match.group(1),
                ).strip()

                if title:
                    return title

        except requests.RequestException:
            pass

        # Fallback: use last part of URL
        slug = self.base_url.rstrip("/").split("/")[-1]

        if slug:
            return slug.replace("-", " ").title()

        return "Documentation"


def detect_site(url: str) -> SiteAdapter:

    response = requests.get(
        url,
        timeout=15,
    )

    response.raise_for_status()

    html = response.text

    if "$docsify" in html:
        return DocsifySite(url)

    raise RuntimeError(
        f"Unsupported documentation framework: {url}"
    )
