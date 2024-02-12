import numpy as np

A = np.array([[-36, 30, 7, 7],
              [7, -38, 0, 5],
              [-10, -19, 33, -18],
              [48, 49, 26, 22]])
y = np.array([-7, -44, 1, 7])

A_inv = np.linalg.inv(A)

result = A_inv @ y

print(result)
