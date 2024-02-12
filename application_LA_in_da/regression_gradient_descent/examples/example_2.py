import numpy as np
from matplotlib import pyplot as plt

X = np.array([[1, 1],
              [4, 1],
              [-3, 1],
              [-5, 1]])
y = np.array([3, 4, -5, -2])


# Функция потерь.
def mse(X, y, w):
    return np.linalg.norm(X @ w - y) ** 2 / len(X)


# Градиент функции потерь.
def grad(X, y, w):
    return 2 * X.T @ (X @ w - y) / len(X)


# Начальные значения параметров.
w = np.array([-1, 5])

# Коэффициент размера шага.
gamma = 1e-2


# Функция для построения графика
def plot_regression(X, y, w):
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], y, s=100)
    x_min, x_max = -10, 10
    y_min, y_max = -10, 10
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    y_min_line = x_min * w[0] + w[1]
    y_max_line = x_max * w[0] + w[1]
    plt.plot(
        [x_min, x_max],
        [y_min_line, y_max_line],
        linewidth=3,
        c="C1")

    plt.xlabel("$x$", fontsize=15)
    plt.ylabel("$y$", fontsize=15, rotation=0, labelpad=15)
    plt.grid()
    plt.show()


# Печатаем начальные значения и строим график.
print('w:', w)
print('MSE:', mse(X, y, w))
plot_regression(X, y, w)

# Обновляем веса.
w = w - gamma * grad(X, y, w)

# Печатаем обновлённые значения и строим график.
print('w:', w)
print('MSE:', mse(X, y, w))
plot_regression(X, y, w)

# Обновляем веса.
w = w - gamma * grad(X, y, w)

# Печатаем обновлённые значения и строим график.
print('w:', w)
print('MSE:', mse(X, y, w))
plot_regression(X, y, w)

# Обновляем веса.
w = w - gamma * grad(X, y, w)

# Печатаем обновлённые значения и строим график.
print('w:', w)
print('MSE:', mse(X, y, w))
plot_regression(X, y, w)
