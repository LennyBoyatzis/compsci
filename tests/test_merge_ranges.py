from problems.merge_ranges import merge_ranges


def test_merge_ranges():
    ranges = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    expected = [(0, 1), (3, 8), (9, 12)]
    result = merge_ranges(ranges)
    assert result == expected
