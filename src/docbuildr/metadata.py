from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class BookMetadata:
    """Metadata describing a generated book."""

    title: str

    source: str

    generated: str

    version: str = "0.3.0-alpha2"

    generator: str = "DocBuildr"

    license: str = "Original documentation license"
