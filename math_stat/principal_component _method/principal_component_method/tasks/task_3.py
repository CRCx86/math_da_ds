import numpy as np

data = np.array([
    [29, 7, 9, 2],
    [375, 116, 75, 163],
    [45, 2, 2, 7],
    [73, 2, 0, 0],
    [104, 30, 39, 30],
    [70, 1056, 1238, 472]
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
