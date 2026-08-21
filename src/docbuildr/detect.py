from __future__ import annotations

from enum import Enum

import requests


class Framework(str, Enum):
    DOCSIFY = "docsify"
    MKDOCS = "mkdocs"
    SPHINX = "sphinx"
    DOCUSAURUS = "docusaurus"
    GENERIC = "generic"


def _exists(url: str) -> bool:
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False


def detect_framework(url: str) -> Framework:
    base = url.rstrip("/")

    if _exists(f"{base}/_sidebar.md"):
        return Framework.DOCSIFY

    if _exists(f"{base}/search/search_index.json"):
        return Framework.MKDOCS

    if _exists(f"{base}/searchindex.js"):
        return Framework.SPHINX

    if _exists(f"{base}/__docusaurus"):
        return Framework.DOCUSAURUS

    return Framework.GENERIC
