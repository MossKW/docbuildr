# Contributing to DocBuildr

Thank you for your interest in contributing to DocBuildr.

Whether you are fixing bugs, improving documentation, or implementing new features, your contributions are welcome.

---

# Development Setup

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

Install dependencies

```bash
pip install -e .
```

Install Playwright

```bash
playwright install chromium
```

---

# Development Workflow

Create a feature branch

```bash
git checkout -b feature/my-feature
```

Make your changes.

Verify everything works.

```bash
python -m compileall src

pip install -e .

docbuildr https://gthlab.au/panaroo
```

Commit your changes.

```bash
git add .

git commit -m "feat(renderer): improve table layout"
```

Push your branch.

```bash
git push origin feature/my-feature
```

Open a Pull Request.

---

# Branch Naming

Use descriptive branch names.

Examples

```
feature/syntax-highlight

feature/theme-engine

fix/pdf-layout

docs/readme

refactor/postprocessor
```

---

# Commit Messages

Follow Conventional Commits.

Examples

```
feat(cli): add verbose mode

feat(pdf): improve print layout

fix(renderer): prevent table overflow

docs: update roadmap

refactor(postprocess): simplify table handling
```

---

# Coding Style

General guidelines

- Keep functions small.
- Prefer readability over cleverness.
- Use type hints.
- Use descriptive variable names.
- Avoid duplicated logic.
- Keep modules focused on a single responsibility.

---

# Project Structure

```
crawler
    ↓
preprocessor
    ↓
book builder
    ↓
renderer
    ↓
postprocessor
    ↓
pdf exporter
```

Please keep this architecture clean.

---

# Pull Requests

Before submitting a pull request, ensure that

- [ ] The project builds successfully.
- [ ] `python -m compileall src` passes.
- [ ] `pip install -e .` succeeds.
- [ ] Runtime testing succeeds.
- [ ] No unrelated files are modified.
- [ ] Documentation is updated if necessary.

---

# Reporting Bugs

Please include

- Operating system
- Python version
- DocBuildr version
- Command used
- Expected behavior
- Actual behavior
- Error messages

---

# Feature Requests

Feature requests are welcome.

Please describe

- the problem
- the proposed solution
- why it would benefit users

---

# Code of Conduct

Be respectful.

Constructive discussions help everyone.

Treat contributors with kindness and professionalism.

---

# Thank You

Thank you for helping improve DocBuildr.

Every contribution—large or small—helps make the project better.
