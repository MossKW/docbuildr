from __future__ import annotations

import argparse

from docbuildr import __version__
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
        description=(
            "Generate Markdown, HTML, and PDF books "
            "from online documentation."
        ),
        epilog=(
            "Examples:\n"
            "  docbuildr https://gthlab.au/panaroo\n\n"
            "  docbuildr https://gthlab.au/panaroo "
            "--title \"Panaroo User Guide\"\n\n"
            "  docbuildr https://gthlab.au/panaroo "
            "--output-name panaroo\n\n"
            "  docbuildr https://gthlab.au/panaroo "
            "--html-only\n\n"
            "  docbuildr https://gthlab.au/panaroo "
            "--verbose"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
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
        help="Base output filename (without extension)",
    )

    parser.add_argument(
        "--html-only",
        action="store_true",
        help="Skip PDF generation",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output",
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
