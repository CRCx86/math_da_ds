import numpy as np
import matplotlib.pyplot as plt

X = np.array([[0, 1], [8, 1], [0, 1], [8, 1]])
y = np.array([10, 7, 7, 6])


# Рассчитываем коэффициенты прямой по формуле.
# w — вектор коэффициентов [k, m].
w = np.linalg.inv(X.T @ X) @ X.T @ y

# Также можно сохранить коэффициенты сразу в отдельные переменные.
k, m = np.linalg.inv(X.T @ X) @ X.T @ y

# Рассчитать предсказание для произвольной точки можно по формуле прямой.
x_test = 6
y_pred = w[0] * x_test + w[1]
print(f"Продуктивность через {x_test} часа(ов) после начала смены:")
print(y_pred)


# Код для построения графика, его можно не изменять.
plt.scatter(X[:2, 0], y[:2], s=100, label=f"День 1")
plt.scatter(X[2:, 0], y[2:], s=100, label=f"День 2")
plt.scatter(x_test, y_pred, zorder=10, s=100, label="Тестовая точка (x_test, y_pred)")

x_min = -1; x_max = 9
y_min = x_min * w[0] + w[1]
y_max = x_max * w[0] + w[1]

plt.plot(
    [x_min, x_max],
    [y_min, y_max],
    linewidth=3,
    c="C4",
    label="Наилучшая прямая",
)
plt.grid()
plt.ylim(-1, 11.5)
plt.xlim(-1, 9)
plt.ylabel("😊", rotation=0, fontsize=25, labelpad=20)
plt.xlabel("Часы после начала смены, t", fontsize=15)
plt.legend(loc=3)
