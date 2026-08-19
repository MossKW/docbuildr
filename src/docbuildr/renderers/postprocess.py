from __future__ import annotations

from bs4 import BeautifulSoup


class HTMLPostProcessor:
    """Post-process rendered HTML before exporting."""

    def process(
        self,
        html: str,
    ) -> str:

        soup = BeautifulSoup(
            html,
            "lxml",
        )

        self._process_tables(soup)
        self._process_images(soup)
        self._process_code_blocks(soup)
        self._process_headings(soup)
        self._process_blockquotes(soup)

        return str(soup)

    def _process_tables(
        self,
        soup: BeautifulSoup,
    ) -> None:

        for table in soup.find_all("table"):

            headers = table.find("thead")

            if headers is None:
                continue

            cols = len(headers.find_all("th"))

            classes = set(table.get("class", []))

            classes.add("doc-table")
            classes.add(f"cols-{cols}")

            table["class"] = sorted(classes)

    def _process_images(
        self,
        soup: BeautifulSoup,
    ) -> None:

        for image in soup.find_all("img"):

            classes = set(image.get("class", []))

            classes.add("doc-image")

            image["class"] = sorted(classes)

    def _process_code_blocks(
        self,
        soup: BeautifulSoup,
    ) -> None:

        for pre in soup.find_all("pre"):

            classes = set(pre.get("class", []))

            classes.add("code-block")

            pre["class"] = sorted(classes)

    def _process_headings(
        self,
        soup: BeautifulSoup,
    ) -> None:

        for heading in soup.find_all("h1"):

            classes = set(heading.get("class", []))

            classes.add("chapter-title")

            heading["class"] = sorted(classes)

    def _process_blockquotes(
        self,
        soup: BeautifulSoup,
    ) -> None:

        for quote in soup.find_all("blockquote"):

            classes = set(quote.get("class", []))

            classes.add("doc-blockquote")

            quote["class"] = sorted(classes)
