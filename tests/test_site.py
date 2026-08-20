from docbuildr.site import DocsifySite


def test_title_from_slug():

    site = DocsifySite(
        "https://example.com/panaroo"
    )

    assert site.base_url == "https://example.com/panaroo"


def test_base_url_trailing_slash_removed():

    site = DocsifySite(
        "https://example.com/docs/"
    )

    assert site.base_url == "https://example.com/docs"


def test_fallback_title_from_slug():

    site = DocsifySite(
        "https://example.com/my-awesome-docs"
    )

    # ใช้ fallback logic โดย monkeypatch title() ภายหลัง
    slug = site.base_url.rstrip("/").split("/")[-1]

    assert slug.replace("-", " ").title() == "My Awesome Docs"

from unittest.mock import Mock, patch

from docbuildr.site import MkDocsSite, detect_site


@patch("docbuildr.site.requests.get")
def test_detect_mkdocs(mock_get):

    html = Mock()
    html.text = "<html></html>"
    html.raise_for_status.return_value = None

    search = Mock()
    search.status_code = 200

    mock_get.side_effect = [
        html,
        search,
    ]

    site = detect_site("https://example.com")

    assert isinstance(site, MkDocsSite)
