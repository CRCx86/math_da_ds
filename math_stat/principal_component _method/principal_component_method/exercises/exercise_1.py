import numpy as np

X = np.array([
    [5, 12],
    [2, 5],
    [0, 2],
    [2, 10],
    [6, 25],
    [3, 14],
    [2, 12],
    [3, 23],
    [7, 26],
    [2, 16]
])

cov_mat = np.cov(X.T)

print(cov_mat)
