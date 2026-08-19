# docs2pdf Architecture

Version: 0.3 (Draft)

---

# Vision

docs2pdf is a documentation publishing engine.

The goal of docs2pdf is to transform online documentation into
beautiful printable books while preserving structure, navigation,
figures, tables, code blocks, and cross references.

Current output:

- PDF
- HTML Book

Future outputs:

- EPUB
- DOCX

---

# Goals

docs2pdf should

- Download documentation automatically
- Preserve document hierarchy
- Preserve images
- Preserve code blocks
- Preserve tables
- Generate a printable book
- Generate a browsable HTML book

---

# Non Goals

docs2pdf is NOT

- A markdown editor
- A static site generator
- A website mirroring tool
- A documentation authoring system

---

# Design Principles

Every module should have exactly one responsibility.

Examples

CLI

Responsible for command line interface only.

Crawler

Responsible for downloading source documents only.

Preprocessor

Responsible for cleaning markdown only.

BookBuilder

Responsible for building the logical book.

Renderer

Responsible for converting markdown into HTML.

Exporter

Responsible for exporting HTML into PDF.

---

# Rendering Pipeline

CLI

↓

Site Adapter

↓

Crawler

↓

Preprocessor

↓

BookBuilder

↓

Renderer

↓

Exporter

---

# Data Model

Documentation

↓

Book

↓

Chapter

↓

Markdown

↓

HTML

↓

PDF

---

# Core Models

BookMetadata

Contains

- title
- source
- generated date

Chapter

Contains

- title
- markdown

Docs2PDFConfig

Contains

- theme
- cover
- toc
- bookmarks
- page numbers

---

# Theme System

Theme consists of independent stylesheets.

base.css

Common typography.

cover.css

Cover page.

toc.css

Table of contents.

tables.css

Table formatting.

code.css

Syntax highlighting.

figures.css

Figure styling.

print.css

Printing rules.

---

# Site Adapters

Every documentation framework should implement the same interface.

Supported

- Docsify

Planned

- MkDocs
- Docusaurus
- Sphinx
- GitBook

---

# Folder Structure

docs2pdf/

docs/

src/

templates/

tests/

---

# Coding Standards

Python 3.11+

4-space indentation

Type hints on all public methods

Dataclasses for models

No duplicated business logic

No renderer-specific code inside BookBuilder

No PDF-specific code inside Renderer

---

# Testing Strategy

Every release should

Compile successfully

Generate HTML successfully

Generate PDF successfully

Render images correctly

---

# Release Workflow

Design

↓

Implement

↓

Compile

↓

Test

↓

Commit

↓

Tag

---

# Roadmap

v0.3

Architecture stabilization

v0.4

Book layout

v0.5

Bookmarks

v0.6

Universal documentation support

v1.0

Public release

---

# End of Document
