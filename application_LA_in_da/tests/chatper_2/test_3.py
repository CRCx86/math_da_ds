import numpy as np

a = np.array([
    [10, -19, 34, 5],
    [42, -7, -8, -9],
    [0, -2, 34, 6],
    [5, 29, 6, 11],
])

U, S, Vt = np.linalg.svd(a)

print("Левые сингулярные векторы:")
print(U)
print("Сингулярные значения:")
print(S)
print("Правые сингулярные векторы:")
V = Vt.T
print(V)
