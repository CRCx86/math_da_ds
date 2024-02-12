import numpy as np

# Задаём систему в матричном виде.
A = np.array([[1, 2, 1], [2, 1, 2], [3, 3, 1]])
y = np.array([8, 10, 12])

# Считаем обратную матрицу.
A_inv = np.linalg.inv(A)

# Находим решение системы.
result = A_inv @ y

print("a =", result[0])
print("b =", result[1])
print("c =", result[2])
