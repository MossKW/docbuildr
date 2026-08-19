from pathlib import Path

from docbuildr.crawler import MarkdownPage
from docbuildr.preprocessor import MarkdownPreprocessor
from docbuildr.renderer import MarkdownRenderer


docs = [
    MarkdownPage(
        title="Mermaid Demo",
        path="mermaid.md",
        markdown=r"""# Mermaid Demo

This page demonstrates offline Mermaid rendering.

```mermaid
graph TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Success]
    B -->|No| D[Retry]
    D --> B
```
""",
    )
]

docs = MarkdownPreprocessor().process(docs)

renderer = MarkdownRenderer()

renderer.render(
    docs=docs,
    output=Path("output/mermaid_demo.md"),
    title="Mermaid Demo",
    source="Local Example",
)

print("Done")
