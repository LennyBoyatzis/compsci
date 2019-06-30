from typing import List


def reverse_string_in_place(char_array: List) -> List:
    """Reverses a char array in place

    Args:
        char_array: char array to reverse in place

    Returns:
        Reversed char array
    """
    left = 0
    right = len(char_array) - 1

    while left < right:
        temp = char_array[left]
        char_array[left] = char_array[right]
        char_array[right] = temp

        left += 1
        right -= 1

    return char_array


if __name__ == "__main__":
    char_array = ['h', 'e', 'l', 'l', 'o']
    result = reverse_string_in_place(char_array)
    print("result", result)
