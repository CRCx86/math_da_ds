import numpy as np

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

data_centered = data - np.mean(data, axis=0)

cov_mat = np.cov(data_centered, rowvar=False)

eigen_values, eigen_vectors = np.linalg.eigh(cov_mat)

sorted_index = np.argsort(eigen_values)[::-1]
sorted_eigenvalue = eigen_values[sorted_index]
sorted_eigenvectors = eigen_vectors[:, sorted_index]

n_components = 1
eigenvector_subset = sorted_eigenvectors[:, 0:n_components]
data_reduced = data_centered @ eigenvector_subset

print(data_reduced)
