from __future__ import annotations

from dataclasses import dataclass

import requests

from docbuildr.site import Page


@dataclass(slots=True)
class MarkdownPage:
    title: str
    path: str
    markdown: str


class MarkdownCrawler:
    """Download Markdown pages directly from Docsify."""

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

            output.append(
                MarkdownPage(
                    title=page.title,
                    path=page.path,
                    markdown=response.text,
                )
            )

        return output
