from typing import List


def binary_search(items, target):
    """Finds index of a target item in a list of items

    Args:
        items: list of items to search through
        target: value of the item to find

    Returns: index of the target item
    """
    floor_index = 0
    ceiling_index = len(items)

    while floor_index < ceiling_index:
        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance
        guess_value = items[guess_index]

        if guess_value == target:
            return guess_index

        if guess_value > target:
            ceiling_index = guess_index
        else:
            floor_index = guess_index

    return -1


if __name__ == "__main__":
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 2
    result = binary_search(items, target)
    print(f"{result}")
