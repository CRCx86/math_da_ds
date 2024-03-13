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

data_centered = data - np.mean(data, axis=0)

cov_mat = np.cov(data_centered, rowvar=False)

eigen_values, eigen_vectors = np.linalg.eigh(cov_mat)

sorted_index = np.argsort(eigen_values)[::-1]
# Сортируем собственные значения по убыванию
sorted_eigenvalue = eigen_values[sorted_index]
# Сортируем собственные векторы
sorted_eigenvectors = eigen_vectors[:, sorted_index]

n_components = 2  # Тут нужное нам значение
eigenvector_subset = sorted_eigenvectors[:, 0:n_components]

data_reduced = data_centered @ eigenvector_subset
print(data_reduced)
