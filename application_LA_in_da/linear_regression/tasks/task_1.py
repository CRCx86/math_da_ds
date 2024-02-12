import numpy as np

X = np.array([[-1, 1], [4, 1], [4, 1], [8, 1], [10, 1]])
y = np.array([0, 4, 6, 8, 12])

# Ваш код здесь.
w = np.linalg.inv(X.T @ X) @ X.T @ y

x_test = 6

result = w[0] * x_test + w[1]

print(result)
