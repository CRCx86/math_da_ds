import numpy as np

data = np.array([
    [0.4, -1, 0.08, 1.2, 0, 0.6, -0.11, 0.45, 1.14, 0.03],
    [-1.1, -0.9, -2, 0.13, 0.4, 0.07, -2, 0.08, 1.4, 3.1],
    [0.4, 0.55, -0.3, 1.7, 0.012, -4, -0.8, 2.3, 1.49, 0],
    [3.2, 0.7, -1, -3.13, 2.77, -6, 0.4, 1, 2, 0.95],
    [0.1, -3.5, 2.9, 0.05, 0.49, -1.34, 0.71, 4.12, 0.04, -2],
    [1.35, -0.81, 0.04, 0.14, 2.03, 5.06, 0.03, -0.12, -7.1, 0.5],
    [1.34, -5, 0.216, 0.09, 0.12, -4.1, 2.1, 2.13, -0.93, -0.734]
])

data_centered = data - np.mean(data, axis=0)

cov_mat = np.cov(data_centered, rowvar=False)

eigen_values, eigen_vectors = np.linalg.eigh(cov_mat)

sorted_index = np.argsort(eigen_values)[::-1]
# Сортируем собственные значения по убыванию
sorted_eigenvalue = eigen_values[sorted_index]
# Сортируем собственные векторы
sorted_eigenvectors = eigen_vectors[:, sorted_index]

n_components = 5  # Тут нужное нам значение
eigenvector_subset = sorted_eigenvectors[:, 0:n_components]

data_reduced = data_centered @ eigenvector_subset
print(data_reduced)
