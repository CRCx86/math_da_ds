import numpy as np

A = np.array([[0, 2, 1],
              [0, -1, 1],
              [-1, -3, 1]])
y = np.array([9, -4, 9])

A_inv = np.linalg.inv(A)

result = A_inv @ y

print(result)
