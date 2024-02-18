import numpy as np

a = np.array([
    [3, -9],
    [1, 9]
])

c = a.T @ a
c_vals, c_vecs = np.linalg.eig(c)
S = np.diag(np.sqrt(c_vals))
d = a @ a.T # Добавляем матрицу.
d_vals, d_vecs = np.linalg.eig(d) # Вычисляем её собственные значения и векторы.
print("Левые сингулярные векторы:")
print(d_vecs) #
print("Проверка:")
print((d_vecs @ S @ c_vecs.T).round()) # Выполняем проверку. 