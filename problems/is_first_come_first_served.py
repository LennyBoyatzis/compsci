from typing import List


def is_first_come_first_served(take_out: List,
                               dine_in: List,
                               served_orders: List) -> bool:
    """Checks that orders are served on a first come first served basis

    Args:
        take_out: list of take out orders
        dine_in: list of dine in order
        served_orders: order in which customers were served

    Returns: bool for whether all orders were served on first come first served
    basis
    """
    take_out_index = 0
    dine_in_index = 0
    take_out_max_index = len(take_out) - 1
    dine_in_max_index = len(dine_in) - 1

    for order in served_orders:
        if take_out_index <= take_out_max_index and order == take_out[take_out_index]:
            take_out_index += 1
        elif dine_in_index <= dine_in_max_index and order == dine_in[dine_in_index]:
            dine_in_index += 1
        else:
            return False

    return True


if __name__ == "__main__":
    take_out = [1, 4, 5]
    dine_in = [2, 3, 6]
    served_orders = [1, 2, 3, 4, 5, 6]
    result = is_first_come_first_served(take_out, dine_in, served_orders)
    assert result is True
