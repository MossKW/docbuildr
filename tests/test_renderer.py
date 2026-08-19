from docbuildr.crawler import MarkdownPage
from docbuildr.renderer import MarkdownRenderer


def sample_docs():

    return [
        MarkdownPage(
            title="Introduction",
            path="/introduction",
            markdown="# Introduction\n\nHello World",
        )
    ]


def test_render_creates_markdown_file(tmp_path):

    output = tmp_path / "book.md"

    renderer = MarkdownRenderer()

    renderer.render(
        docs=sample_docs(),
        output=output,
        title="My Book",
        source="https://example.com",
    )

    assert output.exists()


def test_render_creates_html_file(tmp_path):

    output = tmp_path / "book.md"

    renderer = MarkdownRenderer()

    renderer.render(
        docs=sample_docs(),
        output=output,
        title="My Book",
        source="https://example.com",
    )

    assert output.with_suffix(".html").exists()


def test_render_creates_styles_directory(tmp_path):

    output = tmp_path / "book.md"

    renderer = MarkdownRenderer()

    renderer.render(
        docs=sample_docs(),
        output=output,
        title="My Book",
        source="https://example.com",
    )

    assert (tmp_path / "styles").exists()


def test_markdown_contains_content(tmp_path):

    output = tmp_path / "book.md"

    renderer = MarkdownRenderer()

    renderer.render(
        docs=sample_docs(),
        output=output,
        title="My Book",
        source="https://example.com",
    )

    text = output.read_text(encoding="utf-8")

    assert "Hello World" in text


def test_html_contains_title(tmp_path):

    output = tmp_path / "book.md"

    renderer = MarkdownRenderer()

    renderer.render(
        docs=sample_docs(),
        output=output,
        title="My Book",
        source="https://example.com",
    )

    html = output.with_suffix(".html").read_text(
        encoding="utf-8"
    )

    assert "<title>My Book</title>" in html


def test_html_contains_rendered_content(tmp_path):

    output = tmp_path / "book.md"

    renderer = MarkdownRenderer()

    renderer.render(
        docs=sample_docs(),
        output=output,
        title="My Book",
        source="https://example.com",
    )

    html = output.with_suffix(".html").read_text(
        encoding="utf-8"
    )

    assert "Hello World" in html
