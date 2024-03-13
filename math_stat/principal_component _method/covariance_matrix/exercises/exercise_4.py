import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

X = np.array([
    [1, 4, 5, 5],
    [3, 6, 2, 2],
    [2, 10, 12, 0],
    [3, 9, 6, 2],
    [2, 5, 0, 6],
    [0, 8, 3, 3],
    [1, 8, 9, 2],
    [1, 6, 2, 3],
    [2, 8, 10, 7],
    [0, 5, 7, 2]
])


# Получает массив из трёх столбцов и создаёт для него матрицу ковариации
def cov_matrix_4(X):
    x, y, z, w = X[:, 0], X[:, 1], X[:, 2], X[:, 3]
    x_centered = x - x.mean()
    y_centered = y - y.mean()
    z_centered = z - z.mean()
    w_centered = w - w.mean()

    n = len(X)

    cov_xy = x_centered @ y_centered / (n - 1)
    cov_xz = x_centered @ z_centered / (n - 1)
    cov_yz = y_centered @ z_centered / (n - 1)
    cov_xw = w_centered @ x_centered / (n - 1)
    cov_yw = w_centered @ y_centered / (n - 1)
    cov_zw = w_centered @ z_centered / (n - 1)

    x_var = x_centered @ x_centered / (n - 1)
    y_var = y_centered @ y_centered / (n - 1)
    z_var = z_centered @ z_centered / (n - 1)
    w_var = w_centered @ w_centered / (n - 1)

    cov_mat = np.array([
        [x_var, cov_xy, cov_xz, cov_xw],
        [cov_xy, y_var, cov_yz, cov_yw],
        [cov_xz, cov_yz, z_var, cov_zw],
        [cov_xw, cov_yw, cov_zw, w_var]
    ])

    return cov_mat


cov = cov_matrix_4(X)
print(cov)

labs = ['x', 'y', 'z', 'q']  # Даём название строкам и столбцам.

sns.heatmap(
    cov,  # Матрица ковариации.
    annot=True,  # Подписывать ли значения элементов матрицы.
    fmt='g',  # Округление.
    xticklabels=labs,  # Отсечки на оси Х.
    yticklabels=labs  # Отсечки на оси Y.
)
plt.show()
