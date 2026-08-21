from unittest.mock import Mock, patch

from docbuildr.site import MkDocsSite


@patch("docbuildr.site.requests.get")
def test_mkdocs_pages(mock_get):
    response = Mock()

    response.json.return_value = {
        "docs": [
            {
                "location": "index.html",
                "title": "Home",
            },
            {
                "location": "installation/",
                "title": "Installation",
            },
        ]
    }

    response.raise_for_status.return_value = None

    mock_get.return_value = response

    site = MkDocsSite("https://example.com")

    pages = site.pages()

    assert len(pages) == 2

    assert pages[0].title == "Home"
    assert pages[0].path == "index.html"

    assert pages[1].title == "Installation"
    assert pages[1].path == "installation/"
