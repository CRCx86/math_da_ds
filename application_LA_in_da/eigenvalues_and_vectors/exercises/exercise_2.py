# Допишите код здесь.
import numpy as np

a = np.array([
    [0, 9.4, 0, 4],
    [2, 11, 1, 0],
    [0, -2, 7.5, 0],
    [-1.7, 3, 5, 9]
])
w, v = np.linalg.eig(a)

print("Собственные значения:")
print(w)
print("Собственные векторы:")
print(v)
