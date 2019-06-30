from problems.reverse_string_in_place import reverse_string_in_place


def test_reverse_string_in_place():
    char_array = ['h', 'e', 'l', 'l', 'o']
    expected = ['o', 'l', 'l', 'e', 'h']
    result = reverse_string_in_place(char_array)
    assert result == expected
    assert result is char_array
