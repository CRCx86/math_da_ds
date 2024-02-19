import numpy as np

a = np.array([
    [6, 3, -2, 5],
    [3, 11, -4, -7],
    [-2, -4, 5, 1],
    [5, -7, 1, 29],
])

L, Q = np.linalg.eig(a)
L = np.diag(L)
Q_1 = np.linalg.inv(Q)

print("Матрица собственных векторов:")
print(Q)
print("Матрица собственных значений:")
print(L)
print("Матрица, обратная матрице собственных векторов:")
print(Q_1)
print("Проверка:")
print((Q @ L @ Q_1).round())  # проверка с округлением до целых
