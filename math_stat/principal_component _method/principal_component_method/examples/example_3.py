import numpy as np

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

# Центрируем данные
data_centered = data - np.mean(data, axis=0)

# Вычисляем матричное произведение
product = data_centered.T @ data_centered

# Не забываем поделить на (n - 1)
n = data_centered.shape[0]
product = product / (n - 1)
print("Матрица скалярных произведений данных:")
print(product)

# Сравниваем результат с np.cov
cov_mat = np.cov(data, rowvar=False)
print("Матрица ковариации:")
print(cov_mat)

# Разность матриц
print("Разность матриц")
print(product - cov_mat)
