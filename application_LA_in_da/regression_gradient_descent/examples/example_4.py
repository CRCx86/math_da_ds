import numpy as np

# Исходные точки.
x = np.array([0., 1., 2., 3., 4., 5., 6., 7., 8., 0., 1., 2., 3., 4., 5., 6., 7.,
              8., 0., 1., 2., 3., 4., 5., 6., 7., 8., 0., 1., 2., 3., 4., 5., 6.,
              7., 8., 0., 1., 2., 3., 4., 5., 6., 7., 8., 0., 1., 2., 3., 4.])
y = np.array([9., 7.5, 7.5, 10., 5.5, 7.5, 8.5, 5., 5.5, 5., 7.,
              8.5, 8.5, 5., 6.5, 8.5, 3.5, 3., 5.5, 6., 7., 7.,
              5.5, 6., 8.5, 7., 6., 6., 8., 10., 7., 6., 4.5,
              6.5, 4.5, 6.5, 7., 8.5, 6., 6.5, 9.5, 8., 8., 5.,
              3.5, 6., 9., 6.5, 5.5, 8.])


# Функция потерь и её градиент.
def f(X, y, w):
    return np.mean((X @ w - y) ** 2)


def grad(X, y, w):
    return 2 / len(X) * X.T @ (X @ w - y)


# Составляем матрицу X.
X = np.stack([
    x ** 2,
    x,
    np.ones(len(x))
], axis=1)

# Инициализируем веса модели.
w = np.array([1, 2, 3])

# Производим градиентный спуск.
gamma = 1e-3
max_iter = 10000
eps = 1e-5

# Делаем один шаг, чтобы проверить, что мы ещё не в минимуме.
f_old = f(X, y, w)
w = w - gamma * grad(X, y, w)
f_new = f(X, y, w)

# Текущий шаг.
i = 1

# Основной цикл.
while np.abs(f_new - f_old) > eps and i < max_iter:
    # Обновляем веса.
    w = w - gamma * grad(X, y, w)

    # Увеличиваем номер шага и обновляем значения функции.
    i = i + 1
    f_old = f_new
    f_new = f(X, y, w)

result = w
print(result)
print(f(X, y, w))
