import numpy as np

a = np.array([
    [-2, 1, 0],
    [5, 6, 0],
    [0, 0, 4]
])
w, v = np.linalg.eig(a)
print("Собственные значения:")
print(w)
print("Собственные векторы:")
print(v)
