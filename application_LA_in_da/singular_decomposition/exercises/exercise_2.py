import numpy as np

a = np.array([
    [-9, 14, 2],
    [-7, 5, 3],
    [0, 5, 19]
])

c = a.T @ a # Вычисляем нужную матрицу.
c_vals, c_vecs = np.linalg.eig(c) # Её собственные значения и векторы.
# Берём корни собственных значений и строим диагональную матрицу Sigma.
S = np.diag(np.sqrt(c_vals))
print("Сингулярные значения:")
print(S)
print("Правые сингулярные векторы:")
print(c_vecs)