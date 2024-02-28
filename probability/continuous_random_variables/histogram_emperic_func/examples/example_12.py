import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss


def ecdf(a):
    x, counts = np.unique(a, return_counts=True)
    cusum = np.cumsum(counts)
    return x, cusum / cusum[-1]


def adding(x, y, a):
    x = np.insert(x, 0, x[0])
    y = np.insert(y, 0, 0.)

    x = np.insert(x, 0, min(a) - 1)
    y = np.insert(y, 0, 0.)

    x = np.append(x, max(a) + 1)
    y = np.append(y, 1.)
    return x, y


# Строим графики эмпирической и теоретической функций распределения

# Количество значений в выборке
n_size = 2000

mu = 5
sigma = np.sqrt(10)

# Создаём выборку
X = ss.norm(mu, sigma)
X_vals = X.rvs(n_size)
# Количество точек, в которых будем строить функцию распределения
points_number = 50
# Создаём массивы координат точек x и y эмпирической функции распределения
x, y = ecdf(X_vals)
# Добавляем к массивам координат точек x и y крайних точек
x, y = adding(x, y, X_vals)
# Создаём точки по оси x
xCDF = np.linspace(min(X_vals) - 1, max(X_vals) + 1, points_number)
# Создаём координаты y точек функции распределения
yCDF = ss.norm.cdf(xCDF, loc=mu, scale=sigma)
# Строим график эмпирической функции распределения (благодаря drawstyle график строится "ступеньками")
plt.plot(x, y, drawstyle='steps-post')
# Строим график теоретической функции распределения
plt.plot(xCDF, yCDF)
# Добавляем легенду
plt.legend(["Эмпирическая функция распределения", "Исходная функция распределения"], loc='upper left')
plt.show()
