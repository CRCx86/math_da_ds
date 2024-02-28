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


# Набор значений, собранных Максом и Ульяной
X_vals = [2.64, 8.50, 5.40, 2.54, 3.98, 3.49, 8.68, 1.08,
          3.40, 1.81, 9.41, 4.92, 5.865, 1.31, 12.15, 4.50,
          2.20, 1.16, 8.85, 8.57]

# Параметры равномерного распределения
a = 1
b = 12

# Параметр экспоненциального распределения
Lambda = 0.2

# Параметры нормального распределения
mu = 5
sigma = np.sqrt(10)

x, y = ecdf(X_vals)
x, y = adding(x, y, X_vals)

points_number = 100
xCDF = np.linspace(min(x) - np.mean(x), max(x) + np.mean(x), points_number)

# Создание координат y точек функции распределения (нормального)
yCDF1 = ss.norm.cdf(xCDF, mu, sigma)
# Создание координат y точек функции распределения (экспоненциального)
yCDF2 = ss.expon.cdf(xCDF, scale=1 / Lambda)
# Создание координат y точек функции распределения (равномерного)
yCDF3 = ss.uniform.cdf(xCDF, loc=a, scale=b - a)

plt.plot(x, y, drawstyle='steps-post')
# Построение графика теоретической функции распределения (нормального)
plt.plot(xCDF, yCDF1)
# Построение графика теоретической функции распределения (экспоненциального)
plt.plot(xCDF, yCDF2)
# Построение графика теоретической функции распределения (равномерного)
plt.plot(xCDF, yCDF3)
plt.legend(["Эмпирическая функция распределения исходного набора данных",
            "Функция распределения N(5, 10)",
            "Функция распределения Exp(5)",
            "Функция распределения U[1, 12]"], loc='lower right')
plt.show()
