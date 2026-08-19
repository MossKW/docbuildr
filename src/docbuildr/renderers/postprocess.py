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

            classes = list(table.get("class", []))

            classes.append("doc-table")
            classes.append(f"cols-{cols}")

            table["class"] = sorted(set(classes))
