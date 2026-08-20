from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class DocBuildrConfig:
    """Global configuration for DocBuildr."""

    # Input
    url: str

    # Metadata
    title: str = "Documentation"

    # Output
    output_dir: str | Path = "output"
    output_name: str = "book"

    # Build targets
    html: bool = True
    pdf: bool = True
    viewer: bool = True

    # Console
    verbose: bool = False

    # Crawling
    max_pages: int | None = None

    # Theme
    theme: str = "book"

    # Book options
    cover: bool = True
    toc: bool = True
    bookmarks: bool = True
    page_numbers: bool = True
    syntax_highlighting: bool = True

    def __post_init__(self) -> None:
        self.output_dir = Path(self.output_dir)

    @property
    def markdown_file(self) -> Path:
        return self.output_dir / f"{self.output_name}.md"

    @property
    def html_file(self) -> Path:
        return self.output_dir / f"{self.output_name}.html"

    @property
    def pdf_file(self) -> Path:
        return self.output_dir / f"{self.output_name}.pdf"

    @property
    def viewer_file(self) -> Path:
        return self.output_dir / "viewer.html"
