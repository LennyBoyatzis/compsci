from typing import List


def reverse_words(message: List) -> List:
    """Reverses words in a message

    Args:
        message: lists of words to be reversed

    Returns:
        Reversed words in a list
    """
    left = 0
    right = len(message) - 1

    while left < right:
        message[left], message[right] = message[right], message[left]
        left += 1
        right -= 1

    return message


if __name__ == "__main__":
    message = ['c', 'a', 'k', 'e', ' ',
               'p', 'o', 'u', 'n', 'd', ' ',
               's', 't', 'e', 'a', 'l']

    print("message", message)

    result = reverse_words(message)
    print("result", result)
