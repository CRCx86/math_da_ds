import numpy as np

a = np.array([
    [8, 0, 0, 3],
    [0, 5, 0, 0],
    [-2, 0, -1, 0],
    [0, 11, 0, 4]
])
w, v = np.linalg.eig(a)
print("Собственные значения:")
print(w)
print("Собственные векторы:")
print(v)