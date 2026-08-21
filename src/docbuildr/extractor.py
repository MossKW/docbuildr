from __future__ import annotations

from bs4 import BeautifulSoup
from markdownify import markdownify as md


class HTMLExtractor:
    """
    Extract documentation content from HTML pages.

    Supports

    - MkDocs Material
    - MkDocs
    - Docusaurus
    - Sphinx
    - Docsify
    """

    SELECTORS = (
        # MkDocs Material
        "div.md-content__inner",
        # Generic article
        "article",
        # Docusaurus
        ".theme-doc-markdown",
        # Sphinx
        ".rst-content",
        # Generic
        "#content",
        "#main-content",
        ".content",
        "main",
        "body",
    )

    REMOVE_SELECTORS = (
        "script",
        "style",
        "noscript",
        "nav",
        "header",
        "footer",
        "aside",
        ".md-header",
        ".md-sidebar",
        ".md-tabs",
        ".md-search",
        ".md-footer",
        ".md-dialog",
        ".md-consent",
        ".md-announcement",
        ".md-source",
        ".md-top",
        ".md-feedback",
        ".md-comments",
        ".md-social",
        ".md-nav",
        ".pagination",
        ".edit-page",
        ".mdx-code-block",
    )

    def extract(
        self,
        html: str,
    ) -> str:
        soup = BeautifulSoup(
            html,
            "lxml",
        )

        root = None
        best_len = -1

        #
        # Pick the largest matching container
        #
        for selector in self.SELECTORS:
            for candidate in soup.select(selector):
                length = len(
                    candidate.get_text(
                        " ",
                        strip=True,
                    )
                )

                if length > best_len:
                    best_len = length
                    root = candidate

        if root is None:
            root = soup.body or soup

        #
        # Remove layout inside root only
        #
        for selector in self.REMOVE_SELECTORS:
            for tag in root.select(selector):
                tag.decompose()

        #
        # Remove anchor icons
        #
        for tag in root.select(".headerlink, .anchor, .autorefs-anchor"):
            tag.decompose()

        #
        # Remove empty anchors
        #
        for tag in root.find_all("a"):
            if tag.get("id"):
                tag.decompose()

        #
        # Remove Skip to content links
        #
        for tag in root.find_all("a"):
            text = tag.get_text(
                " ",
                strip=True,
            ).lower()

            if text == "skip to content":
                tag.decompose()

        #
        # Remove SVG
        #
        for tag in root.find_all("svg"):
            tag.decompose()

        #
        # Remove buttons
        #
        for tag in root.find_all("button"):
            tag.decompose()

        #
        # Remove duplicate headings
        #
        seen = set()

        for heading in root.find_all(["h1", "h2"]):
            title = heading.get_text(
                " ",
                strip=True,
            )

            if not title:
                heading.decompose()
                continue

            if title in seen:
                heading.decompose()
                continue

            seen.add(title)

        markdown = md(
            str(root),
            heading_style="ATX",
        )

        #
        # Cleanup
        #
        lines = []

        blank = False

        for line in markdown.splitlines():
            line = line.replace("¶", "").rstrip()

            if not line:
                if blank:
                    continue

                blank = True
                lines.append("")
                continue

            blank = False

            if line.strip().lower() == "skip to content" or any(
                x in line
                for x in (
                    "Was this page helpful?",
                    "Thanks for your feedback!",
                    "Help us improve this page",
                )
            ):
                continue

            lines.append(line)

        markdown = "\n".join(lines).strip()

        #
        # Improve MkDocs feature lists
        #
        markdown = self._fix_mkdocs_lists(
            markdown,
        )

        #
        # Fallback
        #
        if len(markdown) < 50:
            markdown = root.get_text(
                "\n",
                strip=True,
            )

        return markdown

    def _fix_mkdocs_lists(
        self,
        markdown: str,
    ) -> str:
        """
        Fix Markdown generated from MkDocs Material feature cards.

        Convert

        * ## Heading

        into

        ## Heading
        """

        output = []

        for line in markdown.splitlines():
            stripped = line.lstrip()

            if stripped.startswith("* ## "):
                output.append(stripped[2:])
            else:
                output.append(line)

        return "\n".join(output)
