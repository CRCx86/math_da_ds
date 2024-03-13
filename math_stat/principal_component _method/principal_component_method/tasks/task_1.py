import numpy as np

eigen_vectors = np.array([
    [-0.11767587, 0.7341049, 0.66663999, -0.05323077],
    [0.7074337, 0.46026766, -0.34948121, 0.40688343],
    [-0.35872204, -0.1341174, 0.15705602, 0.91031007],
    [-0.59750184, 0.48089105, -0.63936486, -0.05429482]
])

eigen_values = np.array([4.95466601, 24.04206126, 64.49984476, 103.3069994])

sorted_index = np.argsort(eigen_values)[::-1]
sorted_eigenvalue = eigen_values[sorted_index]
sorted_eigenvectors = eigen_vectors[:, sorted_index]

# Шаг 5. Создать вектор-признак
n_components = 2  # Тут нужное нам количество признаков
eigenvector_subset = sorted_eigenvectors[:, 0:n_components]
print(eigenvector_subset)
