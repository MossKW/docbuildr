from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class BookMetadata:
    title: str
    source: str
    generated: str
