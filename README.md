# DocBuildr

> Build beautiful PDF books from online documentation.

DocBuildr is a command-line tool that crawls documentation websites, merges pages into a single book, and generates professional-quality Markdown, HTML, and PDF outputs.

Designed for developers, researchers, engineers, and scientists who want offline documentation with clean typography, mathematical rendering, and print-friendly layouts.

---

## Features

- 📖 Crawl documentation websites automatically
- 📚 Merge multiple pages into a single book
- 📝 Generate clean Markdown output
- 🌐 Export standalone HTML
- 📄 Export print-ready PDF
- 🎨 Professional book layout
- 🖼 Responsive images
- 📊 Smart table formatting
- 💻 Optimized code blocks
- 📑 Automatic table of contents
- ➗ Offline KaTeX math rendering
- ✅ Unit-tested core components
- 🔄 GitHub Actions continuous integration
- ⚡ Simple command-line interface

---

## Installation

Clone the repository

```bash
git clone https://github.com/<YOUR_USERNAME>/docbuildr.git

cd docbuildr
```

Create a virtual environment

```bash
python -m venv .venv

source .venv/bin/activate
```

Install

```bash
pip install -e ".[dev]"
```

---

## Requirements

- Python 3.11+
- Playwright
- Chromium browser

Install Chromium

```bash
playwright install chromium
```

---

## Quick Start

Generate a book

```bash
docbuildr https://gthlab.au/panaroo
```

---

## Examples

Run the bundled KaTeX demo

```bash
python examples/math_demo.py
```

The example generates a standalone HTML document demonstrating inline and display mathematics rendered entirely offline.

---

## Command Line Options

Specify a custom title

```bash
docbuildr URL \
    --title "Panaroo User Guide"
```

Generate HTML only

```bash
docbuildr URL \
    --html-only
```

Specify output directory

```bash
docbuildr URL \
    --output-dir build
```

Specify output filename

```bash
docbuildr URL \
    --output-name panaroo
```

Verbose mode

```bash
docbuildr URL \
    --verbose
```

---

## Output

```text
output/

├── book.md
├── book.html
├── book.pdf
└── viewer.html
```

---

## Project Structure

```text
docbuildr/

├── src/
├── templates/
├── tests/
├── examples/
├── .github/
├── LICENSE
├── README.md
├── RELEASE.md
└── pyproject.toml
```

---

## Build Pipeline

```text
Documentation Website

        │

        ▼

Site Adapter

        │

        ▼

MarkdownCrawler

        │

        ▼

MarkdownPreprocessor

        │

        ▼

BookBuilder

        │

        ▼

MarkdownRenderer

        │
        ├── HTML
        ├── Viewer
        └── Vendor Assets

        ▼

PDFExporter
```

---

## Current Features

| Feature | Status |
|----------|:------:|
| Documentation crawler | ✅ |
| Markdown export | ✅ |
| HTML export | ✅ |
| PDF export | ✅ |
| Table of contents | ✅ |
| Cover page | ✅ |
| Smart tables | ✅ |
| Print layout | ✅ |
| Viewer | ✅ |
| Professional CLI | ✅ |
| Offline KaTeX rendering | ✅ |
| Unit tests | ✅ |
| GitHub Actions CI | ✅ |
| Syntax highlighting | 🚧 |
| Theme engine | 🚧 |
| EPUB export | 🚧 |

---

## Roadmap

### Alpha

- Professional CLI
- Professional print layout
- Offline KaTeX
- Mermaid diagrams
- Syntax highlighting

### Beta

- Theme engine
- EPUB export
- Search index
- Plugin system

### Version 1.0

- Stable API
- Multiple documentation platforms
- Production-ready release

---

## Development

Install development dependencies

```bash
pip install -e ".[dev]"
```

Compile source

```bash
python -m compileall src
```

Run tests

```bash
python -m pytest
```

Run coverage

```bash
python -m pytest --cov=docbuildr
```

Run DocBuildr

```bash
docbuildr https://gthlab.au/panaroo
```

---

## Contributing

Contributions are welcome.

Please read **CONTRIBUTING.md** before submitting a pull request.

---

## License

MIT License

---

## Author

Developed by **Moss.kw**

Built with Python, Playwright, and modern web technologies.
