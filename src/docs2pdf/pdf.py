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
                wait_until="load",
            )

            # รอ DOM โหลด
            page.wait_for_load_state("domcontentloaded")

            # รอ Network โหลด
            page.wait_for_load_state("networkidle")

            # รอรูป render
            page.wait_for_timeout(3000)

            # ใช้ CSS สำหรับพิมพ์
            page.emulate_media(media="print")

            # Debug
            page.screenshot(
                path="output/debug.png",
                full_page=True,
            )

            page.pdf(
                path=str(pdf),
                format="A4",
                print_background=True,
                prefer_css_page_size=True,
                margin={
                    "top": "15mm",
                    "bottom": "15mm",
                    "left": "15mm",
                    "right": "15mm",
                },
            )

            browser.close()
