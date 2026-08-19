from docbuildr.renderers.postprocess import HTMLPostProcessor


def test_add_doc_table_class():

    html = """
    <table>
        <thead>
            <tr>
                <th>A</th>
                <th>B</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>2</td>
            </tr>
        </tbody>
    </table>
    """

    processor = HTMLPostProcessor()

    result = processor.process(html)

    assert "doc-table" in result


def test_add_column_class():

    html = """
    <table>
        <thead>
            <tr>
                <th>A</th>
                <th>B</th>
                <th>C</th>
                <th>D</th>
                <th>E</th>
            </tr>
        </thead>
    </table>
    """

    processor = HTMLPostProcessor()

    result = processor.process(html)

    assert "cols-5" in result


def test_existing_class_is_preserved():

    html = """
    <table class="custom">
        <thead>
            <tr>
                <th>A</th>
            </tr>
        </thead>
    </table>
    """

    processor = HTMLPostProcessor()

    result = processor.process(html)

    assert "custom" in result
    assert "doc-table" in result


def test_table_without_header_is_unchanged():

    html = """
    <table>
        <tbody>
            <tr>
                <td>Hello</td>
            </tr>
        </tbody>
    </table>
    """

    processor = HTMLPostProcessor()

    result = processor.process(html)

    assert "doc-table" not in result
