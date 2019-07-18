from typing import List
from functools import reduce


def calculate_product(list_of_ints: List) -> int:
    """Calculates product of a list of ints"""
    return reduce((lambda x, y: x * y), list_of_ints)


# O(n) runtime
# O(1) additional space

# Greedy approach
# Can we do this in O(n)?
# Could we come up with an answer in one pass through the input
# by simply updating the best answer so far
# What additional values would we need to keep updated as we looked
# at each item in the set, in order to be able to update the best answer so far
# in constant time?

def highest_product_of_3(list_of_ints: List) -> int:
    """Calculate the highest product of three numbers

    Args:
        list_of_ints: List of integers

    Returns:
        An int equal to the highest product of three numbers in the list
    """
    if len(list_of_ints) < 3:
        raise ValueError('Less than 3 items!')

    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]

        highest_product_of_3 = max(highest_product_of_3,
                                   current * highest_product_of_2,
                                   current * lowest_product_of_2)

        highest_product_of_2 = max(highest_product_of_2,
                                   current * highest,
                                   current * lowest)

        lowest_product_of_2 = min(lowest_product_of_2,
                                  current * highest,
                                  current * lowest)

        highest = max(highest, current)
        lowest = min(lowest, current)
    return highest_product_of_3


if __name__ == "__main__":
    list_of_ints = [6, 1, 3, 5, 7, 8, 2]
    result = highest_product_of_3(list_of_ints)
    print("Here is the result {}".format(result))
