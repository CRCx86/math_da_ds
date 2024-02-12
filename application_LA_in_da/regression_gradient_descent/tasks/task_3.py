import numpy as np
import matplotlib.pyplot as plt


# Функция для построения графика
def plot_regression(X, y, w):
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], y, s=100)
    x_min, x_max = x.min() - 1, x.max() + 1
    plt.xlim(x_min, x_max)

    y_min, y_max = y.min() - 10, y.max() + 10
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


x = np.array([0.2557998, -0.82278871, -1.16361648, 0.85579685, -0.69733815,
              -0.54406895, -1.28124149, 0.52042371, 1.71720674, -0.33745467,
              -0.2269758, 1.70396408, -0.53006812, -0.24938224, -0.55129735,
              -1.13231603, 0.76156081, 2.2592402, -1.30971222, 0.36207803,
              -0.36090624, -0.18618701, -1.36268102, -1.26748239, 0.53604899])
y = np.array([3.91277199, -39.31178505, -119.021524, 95.66095598,
              -65.56777682, -74.07919279, -131.61841482, 56.87660473,
              147.41013683, -4.78522204, -53.88777902, 151.18176006,
              -66.92484834, -16.43168069, -68.42110725, -95.21112953,
              82.34320708, 185.08911447, -105.45946497, 7.21805878,
              -42.83812492, -7.7427819, -128.76514706, -97.13091417,
              55.98602108])


# Определите функцию потерь.
def mse(X, y, w):
    return np.mean((X @ w - y) ** 2)


# Определите градиент функции потерь.
def grad(X, y, w):
    return 2 / len(X) * X.T @ (X @ w - y)


# Напишите ваш код здесь.
X = np.stack([x, np.ones(len(x))], axis=1)

w = np.array([1, 1])

gamma = 1e-2
eps = 1e-4
max_iter = 1000

f_old = mse(X, y, w)
w = w - gamma * grad(X, y, w)
f_new = mse(X, y, w)

i = 1

while np.abs(f_new - f_old) > eps and i < max_iter:
    w = w - gamma * grad(X, y, w)

    i += 1
    f_old = f_new
    f_new = mse(X, y, w)

print(w)
print(mse(X, y, w))
plot_regression(X, y, w)
