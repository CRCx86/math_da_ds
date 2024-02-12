import numpy as np
from matplotlib import pyplot as plt

x = np.array([0.00933435, 0.26035948, -1.0671459, -0.7095143, -0.42847615,
              -0.03802681, -0.25940925, 0.71250918, 1.15899237, -0.08650432,
              -0.38432692, -0.0936143, 1.73897809, -0.21756982, -1.14816156,
              -0.23163389, -0.30490744, 0.11929787, 0.30330227, 0.75696207])
y = np.array([0.79178637, 0.47964895, -0.42772685, 0.05413973, 0.86601594,
              0.19763612, 0.05444331, 2.05686234, 14.6846186, 0.12522379,
              0.05420086, 0.11262973, 30.89550988, 0.05530835, -0.07700607,
              0.06937965, 0.07044174, 0.27654468, 3.75782477, 10.18336937])


# Ваш код здесь

def mse(X, y, w):
    # Определите функцию подсчёта ошибки.
    return np.mean((X @ w - y) ** 2)


def grad(X, y, w):
    # Определите градиент функции ошибки.
    return 2 / len(X) * X.T @ (X @ w - y)


X = np.stack([
    x ** 3,
    x ** 2,
    x,
    np.ones(len(x))
], axis=1)

w = np.array([2.5, 2.5, 2.5, 2.5])

gamma = 1e-3
max_iter = 10000
eps = 1e-6

f_old = mse(X, y, w)
w = w - gamma * grad(X, y, w)
f_new = mse(X, y, w)

i = 1
while np.abs(f_new - f_old) > eps and i < max_iter:
    w = w - gamma * grad(X, y, w)

    f_old = f_new
    f_new = mse(X, y, w)
    i += 1

print(mse(X, y, w))

# Код для построения графика.
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], y, s=100)
x_min, x_max = x.min() - 1, x.max() + 1
y_min, y_max = y.min() - 5, y.max() + 5
x_line = np.linspace(x_min, x_max, 100)
y_line = sum(x_line ** i * w_ for i, w_ in enumerate(w[::-1]))
plt.plot(
    x_line,
    y_line,
    linewidth=3,
    c="C1")
plt.xlim(-2, 2)
plt.ylim(-5, 40)
plt.xlabel("$x$", fontsize=15)
plt.ylabel("$y$", fontsize=15, rotation=0, labelpad=15)
plt.grid()
plt.show()
