import numpy as np

a = np.array([
    [5, 27, -16],
    [93, 6, -3],
    [14, -56, 38]
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

print("Проверка:")
print((U @ S @ V.T).round())