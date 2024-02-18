import numpy as np

a = np.array([
    [3, -9],
    [1, 9]
])

U, S, Vt = np.linalg.svd(a)

print("Левые сингулярные векторы:")
print(U)
print("Сингулярные значения:")
print(S)
print("Правые сингулярные векторы:")
print(Vt.T)

print("Проверка")
print((U @ np.diag(S) @ Vt).round()) 