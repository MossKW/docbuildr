from __future__ import annotations

from pathlib import Path

from playwright.sync_api import sync_playwright


class PDFExporter:
    """Export HTML to PDF."""

    def export(
        self,
        html: Path,
        pdf: Path,
    ) -> None:

        html = html.resolve()
        pdf = pdf.resolve()

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True,
            )

            page = browser.new_page()

            page.goto(
                html.as_uri(),
                wait_until="networkidle",
            )

            page.emulate_media(
                media="print",
            )

            # Debug HTML ที่ Render แล้ว
            page.screenshot(
                path="output/debug.png",
                full_page=True,
            )

            page.pdf(
                path=str(pdf),
                print_background=True,
                prefer_css_page_size=True,
            )

            browser.close()
