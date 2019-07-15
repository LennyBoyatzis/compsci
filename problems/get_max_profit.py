from typing import List


def get_max_profit(stock_prices: List) -> int:
    """Calculates the max profit for a given set of stock prices

    Args:
        List of stock prices

    Returns: Maximum profit
    """

    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)

    return max_profit


if __name__ == "__main__":
    prices = [1, 5, 3, 2]
    result = get_max_profit(prices)
    assert result == 4
    print("result: {}".format(result))
