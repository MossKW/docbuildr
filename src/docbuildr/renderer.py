from pathlib import Path
from datetime import date
import shutil

import markdown
from jinja2 import Environment, FileSystemLoader

from docbuildr.book import BookBuilder
from docbuildr.crawler import MarkdownPage
from docbuildr.metadata import BookMetadata


class MarkdownRenderer:

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

        # Build the markdown book
        builder = BookBuilder()

        metadata = BookMetadata(
            title=title,
            source=source,
            generated=date.today().strftime("%d %B %Y"),
        )

        text = builder.build(
            docs=docs,
            metadata=metadata,
        )

        # Save merged markdown
        output.write_text(
            text,
            encoding="utf-8",
        )

        # Markdown -> HTML
        html = markdown.markdown(
            text,
            extensions=[
                "tables",
                "toc",
                "fenced_code",
            ],
        )

        # Load HTML template
        env = Environment(
            loader=FileSystemLoader("templates")
        )

        template = env.get_template(
            "book.html"
        )

        final_html = template.render(
            title=metadata.title,
            content=html,
        )

        # Save HTML
        html_file = output.with_suffix(".html")

        html_file.write_text(
            final_html,
            encoding="utf-8",
        )

        # Copy styles directory
        styles_src = Path("templates/styles")
        styles_dst = output.parent / "styles"

        if styles_dst.exists():
            shutil.rmtree(styles_dst)

        shutil.copytree(
            styles_src,
            styles_dst,
        )
