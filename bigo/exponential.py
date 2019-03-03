import time
from bigo.utils import create_input, graph

# O(2^N)
# Exponential time
# Examples: Recursive calc of fibonacci numbers


def O2N(num):
    if (num <= 1):
        return num
    return O2N(num - 2) + O2N(num - 1)


def graph_O2N():
    x_values = []
    y_values = []
    for i in range(10, 100000, 10000):
        input_data = create_input(i)

        start_time = time.time()
        O2N(input_data, 30)
        runtime = time.time() - start_time

        y_values.append(runtime)
        x_values.append(i)

    graph(x_values, y_values, 'Exponential Time O(2^N)')
