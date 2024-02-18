import numpy as np

a = np.array([
    [12, -6, 4],
    [-6, 7, 0],
    [4, 0, -5]
])
L, Q = np.linalg.eig(a) # сначала значения, потом векторы
L = np.diag(L)
Q_1 = np.linalg.inv(Q)
print("Матрица собственных векторов:")
print(Q)
print("Матрица собственных значений:")
print(L)
print("Матрица, обратная матрице собственных векторов:")
print(Q_1)
print("Проверка:")
print((Q @ L @ Q_1).round()) # проверка с округлением до целых