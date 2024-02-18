import numpy as np

a = np.array([
    [3, -9],
    [1, 9]
])

c = a.T @ a
c_vals, c_vecs = np.linalg.eig(c)
indices = np.argsort(c_vals)
indices = indices[::-1]
c_vals = c_vals[indices]
V = c_vecs[:, indices]
S = np.diag(np.sqrt(c_vals))
U = a @ V @ np.linalg.inv(S)

print("Левые сингулярные векторы:")
print(U)
print("Сингулярные значения:")
print(S)
print("Правые сингулярные векторы:")
print(V)
print("Проверка:")
print((U @ S @ V.T).round()) 