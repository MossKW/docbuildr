from __future__ import annotations

from dataclasses import dataclass

import requests

from docbuildr.extractor import HTMLExtractor
from docbuildr.site import Page


@dataclass(slots=True)
class MarkdownPage:
    title: str
    path: str
    markdown: str


class MarkdownCrawler:
    """Download documentation pages."""

    def __init__(self) -> None:
        self.extractor = HTMLExtractor()

    def fetch(
        self,
        pages: list[Page],
    ) -> list[MarkdownPage]:

        output: list[MarkdownPage] = []

        session = requests.Session()

        for page in pages:

            print(f"Downloading: {page.title}")

            try:

                response = session.get(
                    page.markdown_url,
                    timeout=30,
                )

                response.raise_for_status()

            except requests.RequestException as e:

                print(f"⚠️  Skip: {page.title}")
                print(f"    {e}")

                continue

            text = response.text

            #
            # HTML -> Markdown
            #
            if "<html" in text.lower():

                text = self.extractor.extract(
                    text,
                )

            output.append(
                MarkdownPage(
                    title=page.title,
                    path=page.path,
                    markdown=text,
                )
            )

        return output
