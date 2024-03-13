import numpy as np
from matplotlib import pyplot as plt

data = np.array([
    [1, 4, 5, 5, 12],
    [3, 6, 2, 2, 5],
    [2, 10, 12, 0, 2],
    [3, 9, 6, 2, 10],
    [2, 5, 0, 6, 25],
    [0, 8, 3, 3, 14],
    [1, 8, 9, 2, 12],
    [1, 6, 2, 3, 23],
    [2, 8, 10, 7, 26],
    [0, 5, 7, 2, 16]
])

data_centered = data - data.mean(axis=0)
U, S, Vt = np.linalg.svd(data_centered)

n_components = 2
data_compressed = data_centered @ Vt.T[:, 0:n_components]

print(data_compressed)

plt.scatter(data_compressed[:, 0], data_compressed[:, 1], c=data[:, 2])
plt.show()
