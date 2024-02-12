import numpy as np
X = np.array([[-1, 1], [4, 1], [4, 1], [8, 1], [10, 1]])
y = np.array([0, 4, 6, 8, 12])
w = np.array([1, 0.85])

e = y - X @ w

result = e

print(result)
