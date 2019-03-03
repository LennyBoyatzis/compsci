import matplotlib.pyplot as pyplot
import numpy as np


def create_input(size):
    input_data = []
    for i in range(1, size + 1):
        input_data.append(i)
    return input_data


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def graph(x, y, title):
    pyplot.figure(figsize=(7, 5))
    x = np.array(x)
    y = np.array(y)
    pyplot.plot(x, y, 'o-', linewidth=2)
    pyplot.title(title)
    pyplot.xlabel('Input Size')
    pyplot.ylabel('Run Time')
    pyplot.grid(True)
    pyplot.show()
