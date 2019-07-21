from typing import List


def reverse_string(string: List) -> List:
    """Reverses a string

    Args:
        string: any string

    Returns: a reversed string
    """

    # Copy of list in reversed order
    # string[::-1]

    string_len = len(string)
    left_index = 0
    right_index = string_len - 1

    while left_index < right_index:
        tmp_val = string[left_index]
        string[left_index] = string[right_index]
        string[right_index] = tmp_val
        left_index += 1
        right_index -= 1

    return string


if __name__ == "__main__":
    result = reverse_string(['h', 'e', 'l', 'l', 'o', 'p'])
    print(f"result: {result}")
