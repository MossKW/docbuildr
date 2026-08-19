from pathlib import Path
from playwright.sync_api import sync_playwright


class PDFExporter:

    def export(self, html: Path, pdf: Path):

        html_text = html.read_text(encoding="utf-8")

        css = (html.parent / "style.css").read_text(encoding="utf-8")

        # ฝัง CSS เข้าไปเลย
        html_text = html_text.replace(
            '<link rel="stylesheet" href="style.css">',
            f"<style>\n{css}\n</style>",
        )

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True)

            page = browser.new_page()

            page.set_content(
                html_text,
                wait_until="networkidle",
            )

            page.emulate_media(media="print")

            page.pdf(
                path=str(pdf),
                format="A4",
                print_background=True,
                margin={
                    "top": "15mm",
                    "bottom": "15mm",
                    "left": "15mm",
                    "right": "15mm",
                },
            )

            browser.close()
