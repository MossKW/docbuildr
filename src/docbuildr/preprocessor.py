from __future__ import annotations

import re

from docbuildr.crawler import MarkdownPage
from docbuildr.resolver import AssetResolver


class MarkdownPreprocessor:

    def __init__(self):

        self.resolver = AssetResolver()

    def process(
        self,
        docs: list[MarkdownPage],
    ) -> list[MarkdownPage]:

        output = []

        for doc in docs:

            text = doc.markdown

            text = self.fix_markdown_images(
                text,
                doc,
            )

            text = self.fix_html_images(
                text,
                doc,
            )

            text = self.fix_internal_links(text)

            output.append(
                MarkdownPage(
                    title=doc.title,
                    path=doc.path,
                    markdown=text,
                )
            )

        return output

    def fix_markdown_images(
        self,
        text: str,
        doc: MarkdownPage,
    ) -> str:

        pattern = r'!\[(.*?)\]\((.*?)\)'

        def repl(match):

            alt = match.group(1)

            src = match.group(2).strip()

            # Docsify syntax
            if " '" in src:
                src = src.split(" '", 1)[0]

            if ' "' in src:
                src = src.split(' "', 1)[0]

            src = src.strip()

            url = self.resolver.resolve(
                doc.path,
                src,
            )

            return f"![{alt}]({url})"

        return re.sub(
            pattern,
            repl,
            text,
        )

    def fix_html_images(
        self,
        text: str,
        doc: MarkdownPage,
    ) -> str:

        pattern = r'<img([^>]*?)src="([^"]+)"([^>]*)>'

        def repl(match):

            before = match.group(1)

            src = match.group(2)

            after = match.group(3)

            url = self.resolver.resolve(
                doc.path,
                src,
            )

            after = re.sub(
                r'\s*title=":size=[^"]+"',
                "",
                after,
            )

            return (
                f'<img{before}src="{url}"{after}>'
            )

        return re.sub(
            pattern,
            repl,
            text,
        )

    def fix_internal_links(
        self,
        text: str,
    ) -> str:

        return re.sub(
            r'\]\((/[^)]*?\.md)\)',
            ')',
            text,
        )
