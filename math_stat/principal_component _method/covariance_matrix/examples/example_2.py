import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Получает массив из трёх столбцов и создаёт для него матрицу ковариации
def cov_matrix_3(X):
    x, y, z = X[:, 0], X[:, 1], X[:, 2]
    x_centered = x - x.mean()
    y_centered = y - y.mean()
    z_centered = z - z.mean()
    n = len(X)
    cov_xy = x_centered @ y_centered / (n - 1)
    cov_xz = x_centered @ z_centered / (n - 1)
    cov_yz = y_centered @ z_centered / (n - 1)

    x_var = x_centered @ x_centered / (n - 1)
    y_var = y_centered @ y_centered / (n - 1)
    z_var = z_centered @ z_centered / (n - 1)
    cov_mat = np.array([
        [x_var, cov_xy, cov_xz],
        [cov_xy, y_var, cov_yz],
        [cov_xz, cov_yz, z_var]
    ])

    return cov_mat


meals = [1, 3, 2, 3, 2, 0, 1, 1, 2, 0]
profile = [4, 6, 10, 9, 5, 8, 8, 6, 8, 5]
meetings = [5, 2, 12, 6, 0, 3, 9, 2, 10, 7]

data = np.array([meals, profile, meetings])  # Создаём датасет.

cov = cov_matrix_3(data.transpose())
print(cov)

labs = ['meals', 'profile', 'meetings']  # Даём название строкам и столбцам.

sns.heatmap(
    cov,  # Матрица ковариации.
    annot=True,  # Подписывать ли значения элементов матрицы.
    fmt='g',  # Округление.
    xticklabels=labs,  # Отсечки на оси Х.
    yticklabels=labs  # Отсечки на оси Y.
)
plt.show()
