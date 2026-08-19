from __future__ import annotations

from datetime import date
from pathlib import Path
from importlib.resources import files

import markdown
from jinja2 import Environment, FileSystemLoader

from docbuildr.assets import AssetManager
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

        markdown_text = BookBuilder().build(
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

        html = HTMLPostProcessor().process(html)

        template_root = Path(
            str(
                files("docbuildr").joinpath("templates")
            )
        )

        env = Environment(
            loader=FileSystemLoader(template_root),
        )

        template = env.get_template(
            "book.html",
        )

        final_html = template.render(
            title=metadata.title,
            body=html,
            katex=True,
        )

        html_file = output.with_suffix(".html")

        html_file.write_text(
            final_html,
            encoding="utf-8",
        )

        AssetManager().copy_assets(
            output.parent,
        )
