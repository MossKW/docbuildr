<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
    <img src="assets/logo-light.svg" alt="docbuildr" width="420">
  </picture>
</p>

<p align="center">
  <strong>Turn documentation websites into beautiful books.</strong>
</p>

<p align="center">
  Convert documentation websites into clean, offline-friendly <strong>Markdown</strong>, <strong>HTML</strong>, and <strong>PDF</strong> books with a single command.
</p>

<p align="center">

[![PyPI](https://img.shields.io/pypi/v/docbuildr.svg)](https://pypi.org/project/docbuildr/)
[![Python](https://img.shields.io/pypi/pyversions/docbuildr.svg)](https://pypi.org/project/docbuildr/)
[![License](https://img.shields.io/github/license/MossKW/docbuildr)](LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/docbuildr)](https://pypi.org/project/docbuildr/)

</p>

---

## ✨ Features

| Feature | Status |
|---------|:------:|
| Crawl documentation websites | ✅ |
| Merge multiple pages into one book | ✅ |
| Markdown export | ✅ |
| HTML export | ✅ |
| Print-ready PDF export | ✅ |
| Interactive HTML Viewer | ✅ |
| Automatic table of contents | ✅ |
| Syntax-highlighted code blocks | ✅ |
| Mermaid diagrams | ✅ |
| Offline KaTeX rendering | ✅ |
| Automatic image downloading | ✅ |
| Unit-tested core components | ✅ |

---

## 📦 Installation

```bash
pip install docbuildr
playwright install chromium
```

---

## 🚀 Quick Start

```bash
docbuildr https://gthlab.au/panaroo
```

Generated output:

```text
output/
├── book.md
├── book.html
├── viewer.html
└── book.pdf
```

---

## 📚 Supported Content

- Markdown
- Tables
- Images
- Code blocks
- Mermaid diagrams
- KaTeX equations
- Nested headings
- Internal links

---

## 💡 Why docbuildr?

Instead of manually saving web pages or printing documentation to PDF, **docbuildr** automatically:

- 📖 Crawls an entire documentation website
- 📚 Merges every page into a single book
- 📑 Generates a clean table of contents
- 🎨 Preserves syntax highlighting
- 📄 Produces beautiful print-ready PDF
- 🌐 Creates standalone HTML for offline reading

---

## 🛠 Development

```bash
git clone https://github.com/MossKW/docbuildr.git
cd docbuildr

pip install -e ".[dev]"

python -m pytest
python -m build
```

---

## 🗺 Roadmap

| Feature | Status |
|---------|:------:|
| Markdown Export | ✅ |
| HTML Export | ✅ |
| PDF Export | ✅ |
| HTML Viewer | ✅ |
| Mermaid Support | ✅ |
| KaTeX Support | ✅ |
| EPUB Export | 🚧 |
| Search Index | 🚧 |
| Theme Engine | 🚧 |
| Plugin System | 🚧 |

---

## 🤝 Contributing

Contributions are welcome!

Please read **[CONTRIBUTING.md](CONTRIBUTING.md)** before opening an issue or submitting a pull request.

---

## 📄 License

Released under the **MIT License**.

See **[LICENSE](LICENSE)** for details.

---

## 👨‍💻 Author

Developed by **Moss.kw**

GitHub: https://github.com/MossKW
