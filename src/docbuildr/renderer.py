from __future__ import annotations

from datetime import date
from pathlib import Path
import shutil

import markdown
from jinja2 import Environment, FileSystemLoader

from docbuildr.book import BookBuilder
from docbuildr.crawler import MarkdownPage
from docbuildr.metadata import BookMetadata
from docbuildr.renderers import HTMLPostProcessor


class MarkdownRenderer:
    """Render a documentation book to Markdown and HTML."""

    def render(
        self,
        docs: list[MarkdownPage],
        output: Path,
        title: str = "Documentation",
        source: str = "",
    ) -> None:

        output.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        metadata = BookMetadata(
            title=title,
            source=source,
            generated=date.today().strftime("%d %B %Y"),
        )

        builder = BookBuilder()

        markdown_text = builder.build(
            docs=docs,
            metadata=metadata,
        )

        output.write_text(
            markdown_text,
            encoding="utf-8",
        )

        html = markdown.markdown(
            markdown_text,
            extensions=[
                "tables",
                "toc",
                "fenced_code",
            ],
        )

        processor = HTMLPostProcessor()

        html = processor.process(html)

        env = Environment(
            loader=FileSystemLoader("templates"),
        )

        template = env.get_template(
            "book.html",
        )

        final_html = template.render(
            title=metadata.title,
            content=html,
        )

        html_file = output.with_suffix(".html")

        html_file.write_text(
            final_html,
            encoding="utf-8",
        )

        styles_src = Path("templates/styles")
        styles_dst = output.parent / "styles"

        if styles_dst.exists():
            shutil.rmtree(styles_dst)

        shutil.copytree(
            styles_src,
            styles_dst,
        )
