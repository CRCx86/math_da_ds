import numpy as np
import matplotlib.pyplot as plt

data = np.array([
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

data_centered = data - data.mean(axis=0)
U, S, Vt = np.linalg.svd(data_centered)

n_components = 1
data_compressed = data_centered @ Vt.T[:, 0:n_components]

print(data_compressed)