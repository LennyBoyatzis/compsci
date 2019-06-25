from typing import List


def binary_search(target: int, nums: List[int]) -> int:
    """Returns index of target within a sorted list

    Args:
        target: The target value to find
        nums: The list to find the target within

    Returns:
        The index of the target value within nums list

    """
    floor_index = -1
    ceiling_index = len(nums)

    while floor_index + 1 < ceiling_index:
        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance
        guess_value = nums[guess_index]

        if guess_value == target:
            return guess_index

        if guess_value > target:
            ceiling_index = guess_index
        else:
            floor_index = guess_index

    return -1
