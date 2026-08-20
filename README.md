# DocBuildr

```{=html}
<p align="center">
```
`<strong>`{=html}Convert documentation websites into beautiful Markdown,
HTML, and PDF books.`</strong>`{=html}
```{=html}
</p>
```
```{=html}
<p align="center">
```
[![PyPI](https://img.shields.io/pypi/v/docbuildr.svg)](https://pypi.org/project/docbuildr/)
[![Python](https://img.shields.io/pypi/pyversions/docbuildr.svg)](https://pypi.org/project/docbuildr/)
[![License](https://img.shields.io/github/license/MossKW/docbuildr)](LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/docbuildr)](https://pypi.org/project/docbuildr/)

```{=html}
</p>
```
DocBuildr is a command-line tool that crawls documentation websites,
merges pages into a single book, and generates professional-quality
**Markdown**, **HTML**, and **PDF** outputs.

Designed for developers, researchers, engineers, and scientists who need
clean, offline documentation with print-ready formatting.

------------------------------------------------------------------------

## Features

-   📖 Crawl documentation websites automatically
-   📚 Merge multiple pages into a single book
-   📝 Generate Markdown
-   🌐 Generate standalone HTML
-   📄 Generate print-ready PDF
-   🖥 Interactive HTML Viewer
-   📑 Automatic table of contents
-   💻 Syntax-highlighted code blocks
-   ➗ Offline KaTeX rendering
-   📊 Smart table formatting
-   🖼 Automatic image downloading
-   ✅ Unit-tested core components

------------------------------------------------------------------------

## Installation

``` bash
pip install docbuildr
```

Install Chromium:

``` bash
playwright install chromium
```

------------------------------------------------------------------------

## Quick Start

``` bash
docbuildr https://gthlab.au/panaroo
```

``` text
output/
├── book.md
├── book.html
├── viewer.html
└── book.pdf
```

------------------------------------------------------------------------

## Supported Content

-   Markdown
-   Tables
-   Code blocks
-   Images
-   Mermaid diagrams
-   KaTeX equations
-   Nested headings
-   Internal links

------------------------------------------------------------------------

## Development

``` bash
git clone https://github.com/MossKW/docbuildr.git
cd docbuildr
pip install -e ".[dev]"
python -m pytest
python -m build
```

------------------------------------------------------------------------

## Roadmap

-   [x] Markdown export
-   [x] HTML export
-   [x] PDF export
-   [x] HTML Viewer
-   [x] Mermaid support
-   [x] KaTeX support
-   [ ] EPUB export
-   [ ] Search index
-   [ ] Theme engine
-   [ ] Plugin system

------------------------------------------------------------------------

## Contributing

Contributions are welcome.

Please read **CONTRIBUTING.md** before submitting a pull request.

------------------------------------------------------------------------

## License

MIT License

------------------------------------------------------------------------

## Author

Developed by **Moss.kw**
