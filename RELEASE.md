# Release Process

This document describes the release workflow for DocBuildr.

---

# Release Checklist

Before creating a release, verify the following:

- [ ] Working tree is clean
- [ ] `python -m compileall src` passes
- [ ] `pip install -e .` succeeds
- [ ] `docbuildr --version` works
- [ ] `docbuildr --help` works
- [ ] CI passes
- [ ] README.md updated
- [ ] CHANGELOG.md updated
- [ ] ROADMAP.md updated (if applicable)
- [ ] Version updated in `pyproject.toml`
- [ ] Version updated in `src/docbuildr/__init__.py`

---

# Local Validation

Run the following commands before every release:

```bash
python -m compileall src

pip install -e .

docbuildr --version

docbuildr --help
```

---

# Git Status

Verify repository status.

```bash
git status

git log --oneline -5
```

Working tree should be clean.

---

# Create Release Tag

Example:

```bash
git tag v0.3.0-alpha5
```

Verify:

```bash
git tag
```

---

# Push

Push commits first.

```bash
git push origin feature/professional-cli
```

Push tags.

```bash
git push origin --tags
```

---

# GitHub Release

Create a GitHub Release from the latest tag.

Include:

- Release title
- Highlights
- Bug fixes
- Known limitations

---

# Release Notes Template

## Added

-

## Changed

-

## Fixed

-

## Known Issues

-

---

# After Release

Update:

- ROADMAP.md
- CHANGELOG.md

Create the next development milestone.

Example:

```
v0.3.0-alpha5
↓

v0.3.0-beta1
```
