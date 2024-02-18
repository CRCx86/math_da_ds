import numpy as np

a = np.array([
    [-8, 4, -16],
    [2, 12, 5],
    [-8, 29, 30]
])

U, S, Vt = np.linalg.svd(a)

print("Левые сингулярные векторы:")
print(U)
print("Сингулярные значения:")
print(S)
print("Правые сингулярные векторы:")
V = Vt.T
print(V)

