from pathlib import Path


class DocsifyViewer:
    def create(
        self,
        markdown: Path,
        output: Path,
    ) -> None:
        html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Documentation</title>
</head>
<body>
<p>Viewer placeholder</p>
</body>
</html>
"""

        output.write_text(
            html,
            encoding="utf-8",
        )
