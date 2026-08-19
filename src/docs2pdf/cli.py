from pathlib import Path
import argparse

from docs2pdf.crawler import MarkdownCrawler
from docs2pdf.renderer import MarkdownRenderer
from docs2pdf.site import detect_site
from docs2pdf.preprocessor import MarkdownPreprocessor
from docs2pdf.pdf import PDFExporter
from docs2pdf.viewer import DocsifyViewer


def main():

    parser = argparse.ArgumentParser(
        description="Download Docsify documentation"
    )

    parser.add_argument(
        "url",
        help="Documentation URL",
    )

    args = parser.parse_args()

    site = detect_site(args.url)

    pages = site.pages()

    print(f"Found {len(pages)} pages")

    crawler = MarkdownCrawler()

    docs = crawler.fetch(pages)

    processor = MarkdownPreprocessor()

    docs = processor.process(docs)

    print()
    print("=" * 60)
    print(f"Downloaded {len(docs)} markdown pages")
    print("=" * 60)

    renderer = MarkdownRenderer()

    output = Path("output/book.md")

    renderer.render(
        docs=docs,
        output=output,
        title="Documentation",
        source=args.url,
    )

    print(f"\n✅ Saved: {output}")
    print(f"✅ Saved: {output.with_suffix('.html')}")

    # Create Docsify viewer
    viewer = DocsifyViewer()

    viewer.create(
        output,
        output.with_name("viewer.html"),
    )

    print(f"✅ Saved: {output.with_name('viewer.html')}")

    exporter = PDFExporter()

    pdf_file = output.with_suffix(".pdf")

    exporter.export(
        output.with_suffix(".html"),
        pdf_file,
    )

    print(f"✅ Saved: {pdf_file}")


if __name__ == "__main__":
    main()
