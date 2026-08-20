# DocBuildr

> Build beautiful PDF books from online documentation.

DocBuildr is a command-line tool that crawls documentation websites,
merges pages into a single book, and generates professional-quality
Markdown, HTML, and PDF outputs.

Designed for developers, researchers, engineers, and scientists who want
offline documentation with clean typography, mathematical rendering, and
print-friendly layouts.

------------------------------------------------------------------------

## Features

-   📖 Crawl documentation websites automatically
-   📚 Merge multiple pages into a single book
-   📝 Generate clean Markdown output
-   🌐 Export standalone HTML
-   📄 Export print-ready PDF
-   🎨 Professional book layout
-   🖼 Responsive images
-   📊 Smart table formatting
-   💻 Optimized code blocks
-   📑 Automatic table of contents
-   ➗ Offline KaTeX math rendering
-   ✅ Syntax highlighting
-   ✅ Unit-tested core components
-   🔄 GitHub Actions continuous integration
-   ⚡ Simple command-line interface

------------------------------------------------------------------------

## Installation

Install from PyPI

``` bash
pip install docbuildr
```

Install Chromium

``` bash
playwright install chromium
```

Or install the latest development version

``` bash
git clone https://github.com/MossKW/docbuildr.git
cd docbuildr
pip install -e ".[dev]"
```

------------------------------------------------------------------------

## Requirements

-   Python 3.11+
-   Playwright
-   Chromium browser

------------------------------------------------------------------------

## Quick Start

``` bash
docbuildr https://gthlab.au/panaroo --title "Panaroo User Guide"
```

Produces

``` text
output/
├── book.md
├── book.html
├── book.pdf
└── viewer.html
```

------------------------------------------------------------------------

## Current Features

  Feature                    Status
  ------------------------- --------
  Documentation crawler        ✅
  Markdown export              ✅
  HTML export                  ✅
  PDF export                   ✅
  Table of contents            ✅
  Cover page                   ✅
  Smart tables                 ✅
  Print layout                 ✅
  Viewer                       ✅
  Professional CLI             ✅
  Offline KaTeX rendering      ✅
  Syntax highlighting          ✅
  Unit tests                   ✅
  GitHub Actions CI            ✅
  Theme engine                 🚧
  EPUB export                  🚧
  Search index                 🚧
  Plugin system                🚧

------------------------------------------------------------------------

## Roadmap

### Upcoming

-   Theme engine
-   EPUB export
-   Search index
-   Plugin system

------------------------------------------------------------------------

## Development

``` bash
pip install -e ".[dev]"
python -m compileall src
python -m pytest
python -m pytest --cov=docbuildr
```

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

Built with Python, Playwright, and modern web technologies.
