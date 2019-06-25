from problems.binary_search import binary_search


def test_binary_search():
    result = binary_search(8, [5, 7, 8, 9, 21])
    expected = 2
    assert result == expected
