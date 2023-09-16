
import numpy as np
import matplotlib.pyplot as plt

def plot_graph(function, x_range=(-10, 10), num_points=1000):
    x_values = np.linspace(x_range[0], x_range[1], num_points)
    y_values = function(x_values)

    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph Plotter')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Example function: f(x) = x^2
    function = lambda x: x**2

    # Plot the graph for the given function
    plot_graph(function)
