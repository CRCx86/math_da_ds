# Допишите код здесь.
import numpy as np

a = np.array([
    [-12, 0, 4, 2],
    [6, 8, -5, 1],
    [3, 2, -3, 0],
    [9, 1, 4, 0]
])
w, v = np.linalg.eig(a)

print("Собственные значения:")
print(w)
print("Собственные векторы:")
print(v)
