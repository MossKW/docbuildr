from __future__ import annotations

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass

import requests


@dataclass(slots=True)
class Page:
    title: str
    path: str
    markdown_url: str


class SiteAdapter(ABC):
    """Base class for supported documentation sites."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    @abstractmethod
    def pages(self) -> list[Page]:
        ...

    @abstractmethod
    def title(self) -> str:
        ...


class DocsifySite(SiteAdapter):
    """Docsify documentation."""

    def pages(self) -> list[Page]:
        response = requests.get(
            f"{self.base_url}/_sidebar.md",
            timeout=30,
        )
        response.raise_for_status()

        sidebar = response.text

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
        return fetch_title(self.base_url)


class MkDocsSite(SiteAdapter):
    """MkDocs documentation."""

    def pages(self) -> list[Page]:
        response = requests.get(
            f"{self.base_url}/search/search_index.json",
            timeout=30,
        )
        response.raise_for_status()

        data = response.json()

        pages: list[Page] = []
        seen: set[str] = set()

        for doc in data.get("docs", []):
            location = doc.get(
                "location",
                "",
            ).split(
                "#", 1
            )[0]

            location = location.lstrip("/")

            if location in seen:
                continue

            seen.add(location)

            title = doc.get("title") or location or "Documentation"

            pages.append(
                Page(
                    title=title,
                    path=location,
                    markdown_url=f"{self.base_url}/{location}",
                )
            )

        return pages

    def title(self) -> str:
        return fetch_title(self.base_url)


class GenericSite(SiteAdapter):
    """
    Placeholder for generic HTML documentation.

    This will become the default fallback in v1.1.
    """

    def pages(self) -> list[Page]:
        raise RuntimeError("Generic HTML support is not implemented yet.")

    def title(self) -> str:
        return fetch_title(self.base_url)


def fetch_title(url: str) -> str:
    """
    Return a human-readable documentation title.
    """

    try:
        response = requests.get(
            url,
            timeout=15,
        )

        response.raise_for_status()

        html = response.text

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

    slug = url.rstrip("/").split("/")[-1]

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

    #
    # Docsify
    #
    if "$docsify" in html:
        return DocsifySite(url)

    #
    # MkDocs
    #
    try:
        search = requests.get(
            f"{url.rstrip('/')}/search/search_index.json",
            timeout=5,
        )

        if search.status_code == 200:
            return MkDocsSite(url)

    except requests.RequestException:
        pass

    raise RuntimeError(f"Unsupported documentation framework: {url}")
