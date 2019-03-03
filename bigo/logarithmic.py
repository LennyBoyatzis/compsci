import time
from bigo.utils import create_input, graph

# O(log n)
# Logarithmic time
# Examples: Finding an element in a sorted array (binary search)


def Ologn(input_data, target):
    lower = 0
    upper = len(input_data)
    while lower < upper:
        x = lower + (upper - lower)
        val = input_data[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:
                break
            lower = x
        elif target < val:
            upper = x


def graph_Ologn():
    x_values = []
    y_values = []
    for i in range(10, 100000, 10000):
        input_data = create_input(i)

        start_time = time.time()
        Ologn(input_data, 30)
        runtime = time.time() - start_time

        y_values.append(runtime)
        x_values.append(i)

    graph(x_values, y_values, 'Logarithmic Time O(log n)')
