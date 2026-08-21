from docbuildr.cli import filter_pages
from docbuildr.config import DocBuildrConfig
from docbuildr.site import Page


def test_filter_pages_max_pages():
    pages = [
        Page("A", "a", "a"),
        Page("B", "b", "b"),
        Page("C", "c", "c"),
    ]

    config = DocBuildrConfig(
        url="https://example.com",
        max_pages=2,
    )

    filtered = filter_pages(
        pages,
        config,
    )

    assert len(filtered) == 2
    assert filtered[0].title == "A"
    assert filtered[1].title == "B"
