import numpy as np

a = np.array([
    [2, 11],
    [7, 0]
])

U, S, V = np.linalg.svd(a)

print("Левые сингулярные векторы:")
print(U)
print("Сингулярные значения:")
print(S)
print("Правые сингулярные векторы:")
print(V.T)

print("Проверка")
print((U @ np.diag(S) @ V).round())