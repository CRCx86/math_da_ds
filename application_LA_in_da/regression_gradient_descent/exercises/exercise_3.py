import numpy as np

x = np.array([-9.93841085, -8.2398223, -9.06505398, -7.35203062, -5.82847285,
              -5.08181713, -3.37174708, -3.6361873, -0.06175255, 0.09106786,
              1.46721029, 0.41053496, 1.71012239, 1.84871104, 6.68526793,
              6.82543486, 6.64741998, 8.01775519, 8.57773967, 11.8291112])
y = np.array([0.99747243, 3.28729745, 2.0644648, 2.88068415, -0.05454181,
              0.63703982, 0.06238763, 0.25253028, 0.06582577, 0.05755049,
              0.20686123, -0.03885818, 0.40837474, 0.52833438, 0.25072492,
              0.26994154, 0.29157405, 0.52908138, -0.04000158, -0.98596774])


# Определите функцию для подсчёта ошибки.
def f(X, y, w):
    return np.mean((X @ w - y) ** 2)


# Определите функцию для подсчёта градиента.
def grad(X, y, w):
    return 2 / len(X) * X.T @ (X @ w - y)


# Составляем матрицу X.
X = np.stack([
    x ** 3,
    x ** 2,
    x,
    np.ones(len(x))
], axis=1)

# Инициализируем веса модели.
w = np.array([0.01, 0.01, 0.01, 0.01])

# Производим градиентный спуск.
gamma = 1e-6
max_iter = 10000
eps = 1e-6

# Делаем один шаг, чтобы проверить, что мы ещё не в минимуме.
f_old = f(X, y, w)
w = w - gamma * grad(X, y, w)
f_new = f(X, y, w)

# Текущий шаг.
i = 1

while np.abs(f_new - f_old) > eps and i < max_iter:
    # Обновляем веса.
    w = w - gamma * grad(X, y, w)

    # Увеличиваем номер шага и обновляем значения функции.
    i += 1
    f_old = f_new
    f_new = f(X, y, w)

result = w
print(result)
print(f(X, y, w))
