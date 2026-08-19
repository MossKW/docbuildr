# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog** and this project follows **Semantic Versioning (SemVer)**.

---

## [Unreleased]

### Added

- Placeholder for upcoming features.

---

## [0.3.0-alpha4] - 2026-08-19

### Added

- Semantic HTML post-processing.
- Professional print layout improvements.
- Semantic CSS classes for tables, images, code blocks, headings, and blockquotes.

### Changed

- Improved PDF print layout.
- Improved chapter separation.
- Improved page-break behavior for print output.

### Fixed

- Prevent tables from overflowing pages where possible.
- Prevent images from breaking across pages.
- Prevent code blocks from splitting across pages.

---

## [0.3.0-alpha3] - 2026-08-19

### Added

- Professional command-line interface.
- `--title`
- `--output-dir`
- `--output-name`
- `--html-only`
- `--verbose`

### Changed

- Introduced centralized `DocBuildrConfig`.
- Improved build summary output.

### Fixed

- Fixed output path handling.
- Fixed runtime configuration issues.
- Fixed CLI runtime errors.

---

## [0.3.0-alpha2] - 2026-08-18

### Added

- Project renamed from **docs2pdf** to **DocBuildr**.
- New package name `docbuildr`.
- New HTML template structure.
- Modular stylesheet organization.

### Changed

- Reorganized project layout.
- Improved renderer architecture.

### Removed

- Legacy stylesheet.
- Old package namespace.

---

## [0.3.0-alpha1] - 2026-08-18

### Added

- Initial crawler.
- Markdown aggregation.
- HTML renderer.
- PDF exporter.
- Documentation viewer.
- Cover page.
- Table of contents.
- Basic CSS theme.
