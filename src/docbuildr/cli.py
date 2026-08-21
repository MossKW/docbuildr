from __future__ import annotations

import argparse

from docbuildr import __version__
from docbuildr.config import DocBuildrConfig
from docbuildr.crawler import MarkdownCrawler
from docbuildr.pdf import PDFExporter
from docbuildr.preprocessor import MarkdownPreprocessor
from docbuildr.renderer import MarkdownRenderer
from docbuildr.site import Page, detect_site
from docbuildr.viewer import DocsifyViewer


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="docbuildr",
        description=(
            "Generate Markdown, HTML, and PDF books " "from online documentation."
        ),
        epilog=(
            "Examples:\n"
            "  docbuildr https://gthlab.au/panaroo\n\n"
            "  docbuildr https://gthlab.au/panaroo "
            '--title "Panaroo User Guide"\n\n'
            "  docbuildr https://gthlab.au/panaroo "
            "--output-name panaroo\n\n"
            "  docbuildr https://gthlab.au/panaroo "
            "--html-only\n\n"
            "  docbuildr https://gthlab.au/panaroo "
            "--verbose\n\n"
            "  docbuildr https://gthlab.au/panaroo "
            "--max-pages 10\n\n"
            "  docbuildr https://gthlab.au/panaroo "
            "--include Installation\n\n"
            "  docbuildr https://gthlab.au/panaroo "
            "--exclude FAQ\n\n"
            "  docbuildr https://gthlab.au/panaroo "
            "--docs-only\n\n"
            "  docbuildr https://gthlab.au/panaroo "
            "--include Installation Tutorial "
            "--max-pages 10"
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

    parser.add_argument(
        "--max-pages",
        type=int,
        default=None,
        metavar="N",
        help="Limit the number of pages to download.",
    )

    parser.add_argument(
        "--include",
        nargs="+",
        metavar="KEYWORD",
        help="Include only pages whose title contains one or more keywords.",
    )

    parser.add_argument(
        "--exclude",
        nargs="+",
        metavar="KEYWORD",
        help="Exclude pages whose title contains one or more keywords.",
    )

    parser.add_argument(
        "--docs-only",
        action="store_true",
        help="Skip common non-documentation pages.",
    )

    return parser


def filter_pages(
    pages: list[Page],
    config: DocBuildrConfig,
) -> list[Page]:
    """Apply page filters."""

    if config.docs_only:
        ignored = {
            "blog",
            "changelog",
            "release notes",
            "browser support",
            "conventions",
            "symbols",
            "alternatives",
            "community",
            "sponsor",
            "sponsors",
            "roadmap",
        }

        pages = [page for page in pages if page.title.lower() not in ignored]

    if config.include:
        pages = [
            page
            for page in pages
            if any(keyword.lower() in page.title.lower() for keyword in config.include)
        ]

    if config.exclude:
        pages = [
            page
            for page in pages
            if not any(
                keyword.lower() in page.title.lower() for keyword in config.exclude
            )
        ]

    if config.max_pages is not None:
        pages = pages[: config.max_pages]

    return pages


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
        max_pages=args.max_pages,
        include=args.include,
        exclude=args.exclude,
        docs_only=args.docs_only,
    )

    if config.verbose:
        print("Detecting documentation site...")

    site = detect_site(config.url)

    pages = filter_pages(
        site.pages(),
        config,
    )

    if config.verbose:
        print(f"Found {len(pages)} pages")

    crawler = MarkdownCrawler()
    docs = crawler.fetch(pages)

    #
    # ใช้ base URL ของเว็บปัจจุบัน
    #
    processor = MarkdownPreprocessor(
        config.url,
    )

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
