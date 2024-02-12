import numpy as np

# Задаём систему в матричном виде.
A = np.array([[0, 1], [8, 1]])
y = np.array([10, 7])

# Считаем обратную матрицу.
A_inv = np.linalg.inv(A)

# Находим решение системы.
result = A_inv @ y

print("k =", result[0])
print("m =", result[1])