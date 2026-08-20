from unittest.mock import Mock, patch

from docbuildr.detect import Framework, detect_framework


@patch("docbuildr.detect.requests.get")
def test_detect_mkdocs(mock_get):
    mock_get.return_value = Mock(status_code=404)

    def side_effect(url, timeout=5):
        response = Mock()
        response.status_code = (
            200 if url.endswith("/search/search_index.json") else 404
        )
        return response

    mock_get.side_effect = side_effect

    assert detect_framework("https://example.com") == Framework.MKDOCS
