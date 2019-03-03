import time
from bigo.utils import create_input, graph

# O(N)
# Linear time
# Examples: copy, insert, delete, iteration
# Linear Search


def ON(input_data, target):
    for i in range(len(input_data)):
        if (input_data[i] == target):
            return i
    return -1


def graph_ON():
    x_values = []
    y_values = []
    for i in range(10, 100000, 10000):
        input_data = create_input(i)

        start_time = time.time()
        ON(input_data, 30)
        runtime = time.time() - start_time

        y_values.append(runtime)
        x_values.append(i)

    graph(x_values, y_values, 'Linear Time O(N)')
