from docbuildr.config import DocBuildrConfig
from docbuildr.site import Page

IGNORED_TITLES = {
    "blog",
    "changelog",
    "release notes",
    "browser support",
    "conventions",
    "symbols",
    "alternatives",
    "community",
    "sponsor",
    "sponsors",
    "roadmap",
}


def filter_pages(
    pages: list[Page],
    config: DocBuildrConfig,
) -> list[Page]:
    if config.docs_only:
        pages = [page for page in pages if page.title.lower() not in IGNORED_TITLES]

    if config.include:
        pages = [
            page
            for page in pages
            if any(k.lower() in page.title.lower() for k in config.include)
        ]

    if config.exclude:
        pages = [
            page
            for page in pages
            if not any(k.lower() in page.title.lower() for k in config.exclude)
        ]

    if config.max_pages is not None:
        pages = pages[: config.max_pages]

    return pages
