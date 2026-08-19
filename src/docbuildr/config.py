from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class DocBuildrConfig:
    """Global configuration for DocBuildr."""

    title: str = "Documentation"

    theme: str = "book"

    cover: bool = True

    toc: bool = True

    bookmarks: bool = True

    page_numbers: bool = True

    syntax_highlighting: bool = True
