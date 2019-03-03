import time
from bigo.utils import create_input, graph

# O(N^2)
# Quadratic time
# Examples: 2 Nested loops


def ON2(input_data, target):
    for i in input_data:
        for j in input_data:
            print("i & j")


def graph_ON2():
    x_values = []
    y_values = []
    for i in range(10, 100000, 10000):
        input_data = create_input(i)

        start_time = time.time()
        ON2(input_data, 30)
        runtime = time.time() - start_time

        y_values.append(runtime)
        x_values.append(i)

    graph(x_values, y_values, 'Quadratic Time O(N^2)')
