from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class BookMetadata:
    """Metadata describing a generated book."""

    title: str

    source: str

    generated: str
