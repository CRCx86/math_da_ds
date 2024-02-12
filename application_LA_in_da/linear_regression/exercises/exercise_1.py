import numpy as np
import matplotlib.pyplot as plt

X = np.array([[2, 1], [3, 1], [4, 1], [2.5, 1], [3.5, 1]])
y = np.array([1, 3, 2, 4.5, 3])

x_test = 1.5

# Ваш код здесь.

# Рассчитываем коэффициенты прямой по формуле.
# w — вектор коэффициентов [k, m].
w = np.linalg.inv(X.T @ X) @ X.T @ y

y_pred = w[0] * x_test + w[1]
print(f"Продуктивность через {x_test} часа(ов) после начала смены:")
print(y_pred)

result = y_pred

# Код для построения графика, его можно не менять.
x_min = 1; x_max = 5
y_min = x_min * w[0] + w[1]
y_max = x_max * w[0] + w[1]

plt.scatter(X[:, 0], y, s=100)
plt.vlines(x_test, 0, 5, linestyle='--', color='C1', label="Тестовая точка x_test")
plt.scatter(x_test, result, zorder=10, s=100)
plt.plot(
    [x_min, x_max],
    [y_min, y_max],
    linewidth=3,
    c="C1",
)
plt.xlabel("$x$", fontsize=15)
plt.ylabel("$y$", fontsize=15, rotation=0, labelpad=15)
plt.xlim(x_min, x_max)
plt.ylim(0, 5)
plt.grid()
