import numpy as np

X = np.array([[0, 1, 1], [8, 2, 1], [0, 0, 1], [8, 1, 1]])  # единица — для коэффициента m
y = np.array([10, 7, 7, 6])

w = np.linalg.inv(X.T @ X) @ X.T @ y  # наилучшие коэффициенты
x = np.array([4, 1, 1])  # (4 часа, 1 приём пищи, 1)

result = x @ w
print(f"Коэффициенты прямой: {w}")
print(f"Состояние Макса в середине дня после одного приёма пищи: {result}")
