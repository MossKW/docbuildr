from pathlib import Path

from docbuildr.crawler import MarkdownPage
from docbuildr.renderer import MarkdownRenderer

renderer = MarkdownRenderer()

renderer.render(
    docs=[
        MarkdownPage(
            title="Math Test",
            path="math.md",
            markdown=r"""
# Math Test

Inline math

$E=mc^2$

Display math

$$
\frac{a+b}{c+d}
$$

Matrix

$$
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$
""",
        )
    ],
    output=Path("output/math_test.md"),
    title="KaTeX Demo",
    source="Local Test",
)

print("Done")
