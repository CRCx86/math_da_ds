import numpy as np

data = np.array([
    [2, 2, 2, 2, 2],
    [2, 0, 1, 1, 2],
    [-2, -2, 0, 0, 1],
    [1, 0, 0, 1, 2],
    [-2, -2, -2, 0, -2],
    [1, 1, 1, 1, 1],
    [2, 0, -1, 0, 0]
])

data_centered = data - data.mean(axis=0)
U, S, Vt = np.linalg.svd(data_centered)

n_components = 3
data_compressed = data_centered @ Vt.T[:, 0:n_components]

print(data_compressed)
