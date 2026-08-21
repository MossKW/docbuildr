from pathlib import Path

from docbuildr.config import DocBuildrConfig


def make_config():
    return DocBuildrConfig(
        url="https://example.com",
        output_dir="output",
        output_name="book",
    )


def test_output_dir_is_path():
    config = make_config()

    assert isinstance(config.output_dir, Path)


def test_markdown_file():
    config = make_config()

    assert config.markdown_file == Path("output/book.md")


def test_html_file():
    config = make_config()

    assert config.html_file == Path("output/book.html")


def test_pdf_file():
    config = make_config()

    assert config.pdf_file == Path("output/book.pdf")


def test_viewer_file():
    config = make_config()

    assert config.viewer_file == Path("output/viewer.html")


def test_custom_output_name():
    config = DocBuildrConfig(
        url="https://example.com",
        output_dir="dist",
        output_name="panaroo",
    )

    assert config.markdown_file == Path("dist/panaroo.md")
    assert config.html_file == Path("dist/panaroo.html")
    assert config.pdf_file == Path("dist/panaroo.pdf")


def test_path_output_dir():
    config = DocBuildrConfig(
        url="https://example.com",
        output_dir=Path("build"),
        output_name="docs",
    )

    assert config.output_dir == Path("build")
    assert config.markdown_file == Path("build/docs.md")
