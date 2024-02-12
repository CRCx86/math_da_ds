import numpy as np

X = np.array([[2, 1], [4, 1], [7, 1]])
w = np.array([-0.25, 7.5])
y = np.array([6, 8, 5])

# Расчёт невязок.
e = y - X @ w
print(e)

# Подсчёт ошибки первым подходом.
l_1 = abs(e).mean()
print(l_1)

# Подсчёт ошибки через норму.
l_1 = np.linalg.norm(e, 1) / len(e)
print(l_1)

# средняя квадратичная ошибка
l_2 = (e @ e).sum() / len(e)
print(l_2)

l_2 = np.linalg.norm(e, 2) ** 2 / len(e)
print(l_2)
