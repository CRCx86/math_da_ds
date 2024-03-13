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

cov_mat = np.cov(X.T)

print(cov_mat)