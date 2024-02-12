import numpy as np
X = np.array([[2, 1], [4, 1], [7, 1]])
w = np.array([-0.25, 7.5])
y = np.array([6, 8, 5])

# Расчёт невязок.
e = y - X @ w
print(e)
