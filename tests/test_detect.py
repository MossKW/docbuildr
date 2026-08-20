from docbuildr.detect import Framework


def test_enum():
    assert Framework.DOCSIFY.value == "docsify"
    assert Framework.MKDOCS.value == "mkdocs"
    assert Framework.GENERIC.value == "generic"
