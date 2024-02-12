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

    x_line = np.linspace(x_min, x_max, 100)
    y_line = sum(x_line ** i * w_ for i, w_ in enumerate(w[::-1]))
    plt.plot(
        x_line,
        y_line,
        linewidth=3,
        c="C1")

    plt.xlabel("$x$", fontsize=15)
    plt.ylabel("$y$", fontsize=15, rotation=0, labelpad=15)
    plt.grid()
    plt.show()


x = np.array([0.36511723, -2.29122695, 0.97953661, -0.94396908, -0.96815631,
              -0.16386221, 0.56390546, -0.89312298, -2.60060135, 0.75978944,
              0.33745473, 0.48444799, 3.13062495, -0.08324561, -0.70831587,
              -2.06936933, 1.33635766, 1.95774941, 0.95020456, -0.42779526,
              -0.79792876, -0.97477562, -0.50590791, -1.11005588, 0.61589738,
              -1.00744408, -2.5027091, -2.21920338, 0.31980788, 0.37639869])
y = np.array([2.13522926e+01, 5.06978683e+01, 1.58053673e+00, 2.74510939e+01,
              1.11792249e+01, 1.97241576e-01, 3.25971744e-01, 7.38956279e+00,
              1.12229454e+02, 4.38661842e+00, 1.78254262e-02, 1.38656129e+01,
              1.72499478e+02, 4.02742668e-01, 8.13142320e+00, 1.41003641e+02,
              4.38901544e+01, 9.11764364e+01, 4.53119629e+00, 5.53433512e+00,
              1.06673137e+01, 2.01839095e+01, 2.14197937e+00, 5.48899119e+01,
              1.40324912e+01, 1.84566292e+01, 1.59657382e+02, 7.80859142e+01,
              1.70202093e-01, 3.30858375e+00])


# Функция потерь.
def mse(X, y, w):
    return np.linalg.norm(X @ w - y) ** 2 / len(X)


# Градиент функции потерь.
def grad(X, y, w):
    return 2 * X.T @ (X @ w - y) / len(X)


# Напишите ваш код здесь.
X = np.stack([
    x ** 3,
    x ** 2,
    x,
    np.ones(len(x))
], axis=1)

w = np.array([10, 10, 10, 10])

gamma = 1e-3
max_iter = 10000
eps = 1e-6

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
