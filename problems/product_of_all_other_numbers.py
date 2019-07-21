from typing import List


def get_products_of_all_ints_except_at_index(exclusions: List) -> List:
    """Returns the product of all other ints

    Args:
        exclusions: list of indices

    Returns: List of products
    """

    if len(exclusions) < 2:
        raise ValueError('A list of at least two elements is required')

    product_of_ints = []
    total_with_zeros = 1
    total_without_zeros = 1
    num_zeros = 0

    for i in exclusions:
        total_with_zeros = total_with_zeros * i
        if i == 0:
            num_zeros += 1
        if i != 0:
            total_without_zeros = total_without_zeros * i

    if num_zeros > 1:
        product_of_ints = [0] * len(exclusions)
        return product_of_ints

    for i in exclusions:
        number = total_with_zeros // i if i != 0 else total_without_zeros
        product_of_ints.append(number)

    return product_of_ints


if __name__ == "__main__":
    exclusions = [6, 2, 0, 3]
    result = get_products_of_all_ints_except_at_index(exclusions)
    print(f"Result: {result}")
