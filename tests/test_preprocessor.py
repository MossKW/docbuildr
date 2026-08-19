from docbuildr.preprocessor import MarkdownPreprocessor


def test_fix_mermaid_block():

    processor = MarkdownPreprocessor()

    markdown = """
# Demo

```mermaid
graph TD
A --> B
```
"""

    result = processor.fix_mermaid_blocks(markdown)

    assert '<div class="mermaid">' in result
    assert "graph TD" in result
    assert "A --> B" in result
    assert "</div>" in result


def test_non_mermaid_code_block_is_unchanged():

    processor = MarkdownPreprocessor()

    markdown = """```python
print("hello")
```"""

    result = processor.fix_mermaid_blocks(markdown)

    assert result == markdown


def test_multiple_mermaid_blocks():

    processor = MarkdownPreprocessor()

    markdown = """
```mermaid
graph TD
A --> B
```

Text

```mermaid
graph LR
C --> D
```
"""

    result = processor.fix_mermaid_blocks(markdown)

    assert result.count('<div class="mermaid">') == 2


def test_empty_mermaid_block():

    processor = MarkdownPreprocessor()

    markdown = """
```mermaid
```
"""

    result = processor.fix_mermaid_blocks(markdown)

    assert '<div class="mermaid">' in result
