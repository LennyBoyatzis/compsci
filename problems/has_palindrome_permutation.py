from collections import Counter


def has_palindrome_permutation(string: str) -> bool:
    """Checks whether any permutation of an input string is a palindrome

    Args:
        string: input string to check

    Returns: Boolean as to whether any permutation of the input string is a
    palindrome
    """
    unpaired_characters = set()

    for char in string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    return len(unpaired_characters) <= 1


if __name__ == "__main__":
    result = has_palindrome_permutation('aabbccdd')
    print("result", result)
