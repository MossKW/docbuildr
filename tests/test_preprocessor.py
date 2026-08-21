from docbuildr.preprocessor import MarkdownPreprocessor


processor = MarkdownPreprocessor(
    "https://example.com",
)


def test_fix_mermaid_block():
    text = """
```mermaid
graph TD
A-->B
```
"""

    result = processor.fix_mermaid_blocks(text)

    assert '<div class="mermaid">' in result
    assert "graph TD" in result
    assert "A-->B" in result


def test_non_mermaid_code_block_is_unchanged():
    text = """
```python
print("hello")
```
"""

    result = processor.fix_mermaid_blocks(text)

    assert result == text


def test_multiple_mermaid_blocks():
    text = """
```mermaid
graph TD
A-->B
```

Some text.

```mermaid
graph LR
X-->Y
```
"""

    result = processor.fix_mermaid_blocks(text)

    assert result.count('<div class="mermaid">') == 2


def test_empty_mermaid_block():
    text = """
```mermaid
```
"""

    result = processor.fix_mermaid_blocks(text)

    assert '<div class="mermaid">' in result
