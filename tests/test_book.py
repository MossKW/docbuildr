from docbuildr.book import BookBuilder
from docbuildr.metadata import BookMetadata


def test_build_cover_contains_title():

    metadata = BookMetadata(
        title="Panaroo",
        source="https://example.com",
        generated="19 August 2026",
    )

    builder = BookBuilder()

    cover = builder.build_cover(metadata)

    assert "Panaroo" in cover


def test_build_cover_contains_source():

    metadata = BookMetadata(
        title="Book",
        source="https://example.com",
        generated="Today",
    )

    builder = BookBuilder()

    cover = builder.build_cover(metadata)

    assert "https://example.com" in cover


def test_build_cover_contains_generated_date():

    metadata = BookMetadata(
        title="Book",
        source="Example",
        generated="Today",
    )

    builder = BookBuilder()

    cover = builder.build_cover(metadata)

    assert "Generated on Today" in cover
