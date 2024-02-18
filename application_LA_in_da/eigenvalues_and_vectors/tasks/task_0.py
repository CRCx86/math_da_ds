# Допишите код здесь.
import numpy as np

# a = np.array([
#     [6.75, -4, 52/7],
#     [-0.875, 0.25, -1.5],
#     [-7/32, 1/8, -1/4]
# ])
a = np.array([
    [0.5, 33/28, 1],
    [1, 1/6, 34/63],
    [0, -1, -2/3]
])
w, v = np.linalg.eig(a)

print("Собственные значения:")
print(w)
print("Собственные векторы:")
print(v)