from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Chapter:
    """A single chapter in the generated book."""

    title: str

    markdown: str
