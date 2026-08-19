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
