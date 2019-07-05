from typing import List


def reverse_words(message: List) -> List:
    """Reverses words in a message

    Args:
        message: lists of words to be reversed

    Returns:
        Reversed words in a list
    """
    return ''.join(message).split(' ')[::-1]


def reverse_chars_in_place(message: List) -> List:
    """Reverses chars in a message in place

    Args:
        message: lists of chars to be reversed

    Returns:
        Reversed chars in a list
    """
    left = 0
    right = len(message) - 1

    while left < right:
        message[left], message[right] = message[right], message[left]
        left += 1
        right -= 1

    return message


def reverse_words_in_place(message: List) -> List:
    """Reverses words in a message in place

    Args:
        message: lists of words to be reversed

    Returns:
        Reversed words in a list
    """
    pass


if __name__ == "__main__":
    message = ['c', 'a', 'k', 'e', ' ',
               'p', 'o', 'u', 'n', 'd', ' ',
               's', 't', 'e', 'a', 'l']

    result = reverse_words_in_place(message)
    print("result", result)
