import numpy as np

a = np.array([
    [3, 17, 48],
    [0, -6, 21],
    [9, -5, 39],
    [0, 18, 10]
])

U, S, Vt = np.linalg.svd(a)

print("Левые сингулярные векторы:")
print(U)
print("Сингулярные значения:")
print(S)
print("Правые сингулярные векторы:")
V = Vt.T
print(V)

