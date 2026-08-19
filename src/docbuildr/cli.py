from __future__ import annotations

import argparse

from docbuildr.config import DocBuildrConfig
from docbuildr.crawler import MarkdownCrawler
from docbuildr.pdf import PDFExporter
from docbuildr.preprocessor import MarkdownPreprocessor
from docbuildr.renderer import MarkdownRenderer
from docbuildr.site import detect_site
from docbuildr.viewer import DocsifyViewer


def build_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        prog="docbuildr",
        description="Build beautiful books from documentation.",
        epilog=(
            "Example:\n"
            "  docbuildr https://gthlab.au/panaroo\n\n"
            "Examples:\n"
            "  docbuildr URL --title \"Panaroo Guide\"\n"
            "  docbuildr URL --html-only\n"
            "  docbuildr URL --verbose"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "url",
        help="Documentation URL",
    )

    parser.add_argument(
        "--title",
        default="Documentation",
        help="Book title",
    )

    parser.add_argument(
        "--output-dir",
        default="output",
        help="Output directory (default: output)",
    )

    parser.add_argument(
        "--output-name",
        default="book",
        help="Output filename without extension",
    )

    parser.add_argument(
        "--html-only",
        action="store_true",
        help="Generate Markdown and HTML only",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show progress messages",
    )

    return parser


def main() -> None:

    parser = build_parser()
    args = parser.parse_args()

    config = DocBuildrConfig(
        url=args.url,
        title=args.title,
        output_dir=args.output_dir,
        output_name=args.output_name,
        pdf=not args.html_only,
        verbose=args.verbose,
    )

    if config.verbose:
        print("Detecting documentation site...")

    site = detect_site(config.url)
    pages = site.pages()

    if config.verbose:
        print(f"Found {len(pages)} pages")

    crawler = MarkdownCrawler()
    docs = crawler.fetch(pages)

    processor = MarkdownPreprocessor()
    docs = processor.process(docs)

    renderer = MarkdownRenderer()

    renderer.render(
        docs=docs,
        output=config.markdown_file,
        title=config.title,
        source=config.url,
    )

    if config.viewer:

        viewer = DocsifyViewer()

        viewer.create(
            config.markdown_file,
            config.viewer_file,
        )

    if config.pdf:

        exporter = PDFExporter()

        exporter.export(
            config.html_file,
            config.pdf_file,
        )

    print()
    print("=" * 60)
    print("Build completed successfully.")
    print("=" * 60)

    print(f"Markdown : {config.markdown_file}")
    print(f"HTML     : {config.html_file}")

    if config.viewer:
        print(f"Viewer   : {config.viewer_file}")

    if config.pdf:
        print(f"PDF      : {config.pdf_file}")


if __name__ == "__main__":
    main()
