# DocBuildr

> Build beautiful PDF books from online documentation.

DocBuildr is a command-line tool that crawls documentation websites, merges pages into a single book, and generates professional-quality Markdown, HTML, and PDF outputs.

Designed for developers, researchers, and engineers who want offline documentation with clean typography and print-friendly layouts.

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
pip install -e .
```

Install Playwright browser

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

```
output/

├── book.md
├── book.html
├── book.pdf
└── viewer.html
```

---

## Project Structure

```
docbuildr/

├── crawler.py
├── preprocessor.py
├── book.py
├── renderer.py
├── pdf.py
├── viewer.py
├── cli.py
└── renderers/
```

---

## Build Pipeline

```
Documentation Website

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

        ▼

HTMLPostProcessor

        │

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
| Syntax highlighting | 🚧 |
| KaTeX | 🚧 |
| Theme engine | 🚧 |
| EPUB export | 🚧 |

---

## Roadmap

### Alpha

- Professional CLI
- Professional print layout
- Syntax highlighting
- KaTeX support

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

Run in editable mode

```bash
pip install -e .
```

Compile

```bash
python -m compileall src
```

Run

```bash
docbuildr https://gthlab.au/panaroo
```

---

## Contributing

Contributions are welcome.

Please read

- CONTRIBUTING.md

before submitting a pull request.

---

## License

MIT License

---

## Author

Developed with ❤️ using Python and Playwright.
