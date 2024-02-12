import numpy as np

X = np.array([[0, 1, 1], [8, 2, 1], [0, 0, 1], [8, 1, 1]])
y = np.array([10, 7, 7, 6])

w = np.linalg.inv(X.T @ X) @ X.T @ y
X_test = np.array([[0, 0, 1], [4, 1, 1], [8, 1, 1]])

result = X_test @ w

print(f"Состояние Макса в начале дня: {result[0]:.3f}")
print(f"Состояние Макса в середине дня: {result[1]:.3f}")
print(f"Состояние Макса в конце дня: {result[2]:.3f}")
