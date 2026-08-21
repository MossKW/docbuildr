from __future__ import annotations

import re

from docbuildr.crawler import MarkdownPage
from docbuildr.resolver import AssetResolver


class MarkdownPreprocessor:
    def __init__(
        self,
        base_url: str,
    ) -> None:
        self.resolver = AssetResolver(
            base_url,
        )

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

            text = self.fix_internal_links(
                text,
            )

            text = self.fix_mermaid_blocks(
                text,
            )

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
        pattern = r"!\[(.*?)\]\((.*?)\)"

        def repl(match):
            alt = match.group(1)

            src = match.group(2).strip()

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

            return f'<img{before}src="{url}"{after}>'

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
            r"\]\((/[^)]*?\.md)\)",
            ")",
            text,
        )

    def fix_mermaid_blocks(
        self,
        text: str,
    ) -> str:
        pattern = re.compile(
            r"```mermaid\s*\n(.*?)```",
            flags=re.DOTALL,
        )

        def repl(match):
            diagram = match.group(1).strip()

            return '<div class="mermaid">\n' f"{diagram}\n" "</div>"

        return pattern.sub(
            repl,
            text,
        )
