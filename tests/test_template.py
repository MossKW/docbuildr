from pathlib import Path


def test_book_template_contains_katex():

    template = Path("templates/book.html").read_text(
        encoding="utf-8",
    )

    assert "katex.min.css" in template
    assert "katex.min.js" in template
    assert "auto-render.min.js" in template
    assert "renderMathInElement" in template
