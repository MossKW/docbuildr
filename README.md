<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MossKW/docbuildr/main/assets/logo-dark.svg">
    <img src="https://raw.githubusercontent.com/MossKW/docbuildr/main/assets/logo-light.svg"
         alt="docbuildr"
         width="420">
  </picture>
</p>

<p align="center">
  <strong>Turn documentation websites into beautiful books.</strong>
</p>

<p align="center">
  Convert documentation websites into clean, offline-friendly <strong>Markdown</strong>,
  <strong>HTML</strong>, and <strong>PDF</strong> books with a single command.
</p>

<p align="center">

[![PyPI](https://img.shields.io/pypi/v/docbuildr.svg)](https://pypi.org/project/docbuildr/)
[![Python](https://img.shields.io/pypi/pyversions/docbuildr.svg)](https://pypi.org/project/docbuildr/)
[![License](https://img.shields.io/github/license/MossKW/docbuildr)](LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/docbuildr)](https://pypi.org/project/docbuildr/)

</p>

---

# ✨ Features

| Feature | Status |
|---------|:------:|
| Crawl documentation websites | ✅ |
| Merge multiple pages into one book | ✅ |
| Export Markdown | ✅ |
| Export standalone HTML | ✅ |
| Export print-ready PDF | ✅ |
| Interactive HTML Viewer | ✅ |
| Automatic Table of Contents | ✅ |
| Syntax Highlighting | ✅ |
| Offline KaTeX Rendering | ✅ |
| Mermaid Diagrams | ✅ |
| Smart Table Formatting | ✅ |
| Automatic Image Download | ✅ |

---

# 📦 Installation

```bash
pip install docbuildr
```

Install Chromium (required for PDF generation):

```bash
playwright install chromium
```

---

# 🚀 Quick Start

```bash
docbuildr https://gthlab.au/panaroo
```

Output:

```text
output/
├── book.md
├── book.html
├── viewer.html
└── book.pdf
```

---

# 📚 Supported Content

- Markdown
- Tables
- Images
- Code blocks
- Mermaid diagrams
- KaTeX equations
- Nested headings
- Internal links

---

# 🛠 Development

Clone the repository:

```bash
git clone https://github.com/MossKW/docbuildr.git
cd docbuildr
```

Install development dependencies:

```bash
pip install -e ".[dev]"
```

Run tests:

```bash
pytest
```

Build package:

```bash
python -m build
```

---

# 🗺 Roadmap

- [x] Markdown export
- [x] HTML export
- [x] PDF export
- [x] HTML Viewer
- [x] Mermaid support
- [x] KaTeX support
- [ ] EPUB export
- [ ] Search index
- [ ] Theme engine
- [ ] Plugin system

---

# 🤝 Contributing

Contributions are welcome!

Please read **CONTRIBUTING.md** before submitting a pull request.

---

# 📄 License

Released under the **MIT License**.

---

# 👤 Author

Developed by **Moss.kw**

📧 k.pollapong@gmail.com
