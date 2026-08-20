from __future__ import annotations

import re


class SmartCodeFence:
    """Automatically add language identifiers to fenced code blocks."""

    SHELL_PREFIXES = (
        "pip",
        "pip3",
        "python",
        "python3",
        "conda",
        "mamba",
        "git",
        "docker",
        "sudo",
        "apt",
        "apt-get",
        "brew",
        "cargo",
        "npm",
        "pnpm",
        "yarn",
        "make",
        "cmake",
        "curl",
        "wget",
    )

    def process(
        self,
        markdown: str,
    ) -> str:

        pattern = re.compile(
            r"```[ \t]*\n(.*?)\n```",
            re.DOTALL,
        )

        def replace(
            match: re.Match[str],
        ) -> str:

            block = match.group(1)

            lines = block.splitlines()

            if not lines:
                return match.group(0)

            first = lines[0].strip()

            if any(
                first.startswith(prefix)
                for prefix in self.SHELL_PREFIXES
            ):
                return f"```bash\n{block}\n```"

            return match.group(0)

        return pattern.sub(
            replace,
            markdown,
        )
