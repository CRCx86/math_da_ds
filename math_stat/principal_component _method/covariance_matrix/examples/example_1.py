import numpy as np

X = np.array([
    [1, 4],
    [3, 6],
    [2, 10],
    [3, 9],
    [2, 5],
    [0, 8],
    [1, 8],
    [1, 6],
    [2, 8],
    [0, 5],
])
print("x_mean:", X[:, 0].mean())
print("y_mean:", X[:, 1].mean())
