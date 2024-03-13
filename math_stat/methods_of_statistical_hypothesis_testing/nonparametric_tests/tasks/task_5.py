import numpy as np

X1 = np.array([6, 4, 5, 8, 3, 6, 7, 5])
X2 = np.array([8, 9, 4, 7, 9, 9, 7, 9])

result = X1 - X2
print(result)

result_abs = sorted(np.abs(result))
print(result_abs)
