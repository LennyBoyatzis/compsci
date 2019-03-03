import time
from bigo.utils import create_input, graph

# O(N^3)
# Cubic time
# Examples: 3 Nested loops, matrix multiplication


def ON3(input_data, target):
    for i in input_data:
        for j in input_data:
            for k in input_data:
                print('{}, {}, {}'.format(i, j, k))


def graph_ON3():
    x_values = []
    y_values = []
    for i in range(10, 100000, 10000):
        input_data = create_input(i)

        start_time = time.time()
        ON3(input_data, 30)
        runtime = time.time() - start_time

        y_values.append(runtime)
        x_values.append(i)

    graph(x_values, y_values, 'Cubic Time O(N^3)')
