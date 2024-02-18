import numpy as np

a = np.array([
    [13, 0, -5],
    [-19, 24, -6],
    [3.9, 14, 29]
])

c = a.T @ a
c_vals, c_vecses = np.linalg.eig(c)

indices = np.argsort(c_vals)
indices = indices[::-1]

c_vals = c_vals[indices]

c_vecs = c_vecses[:, indices]
S = np.diag(np.sqrt(c_vals))

print("Сингулярные значения:")
print(S)
print("Правые сингулярные векторы:")
print(c_vecs)
