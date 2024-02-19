# Допишите код здесь.
import numpy as np

a = np.array([
    [2, -5, 0, 6],
    [0, 2, 3, -1],
    [4, 0, -1, 6],
    [5, 0, 3, 0]
])

w, v = np.linalg.eig(a)

print("Собственные значения:")
print(w)
print("Собственные векторы:")
print(v)
