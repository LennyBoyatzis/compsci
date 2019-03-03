import time
from bigo.utils import create_input, graph

# 0(1)
# Constant Time
# No matter size of input, the runtime will always be the same
# Examples: append, get item, set item


def O1(input_data):
    dummy_list = []
    dummy_list.append(input_data)
    return


def graph_O1():
    x_values = []
    y_values = []
    for i in range(10, 100000, 10000):
        input_data = create_input(i)
        start_time = time.time()
        O1(input_data)
        runtime = time.time() - start_time
        y_values.append(runtime)
        x_values.append(i)

    graph(x_values, y_values, 'Constant Time O(1)')
