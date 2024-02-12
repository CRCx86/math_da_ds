import numpy as np
X = np.array([[2, 1], [3, 1], [4, 1], [2.5, 1], [3.5, 1]])
w = np.array([-0.5, 3])
y = np.array([1, 3, 2, 4.5, 3])

e = y - X @ w

result = e

print(result)
