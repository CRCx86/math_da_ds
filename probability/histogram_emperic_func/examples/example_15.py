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


def error_Q(x, y, dist):
    Q = 0
    for i in range(len(x)):
        Q += (y[i] - dist.cdf(x[i])) ** 2
    return Q / len(x)


# График эмпирической и теоретической функций распределения

X_vals = [2.64, 8.50, 5.40, 2.54, 3.98, 3.49, 8.68, 1.08,
          3.40, 1.81, 9.41, 4.92, 5.865, 1.31, 12.15, 4.50,
          2.20, 1.16, 8.85, 8.57]

mu = 5
sigma = np.sqrt(10)

Lambda = 5

a = 1
b = 12

x, y = ecdf(X_vals)
x, y = adding(x, y, X_vals)

points_number = 100
xCDF = np.linspace(min(X_vals) - np.mean(X_vals), max(X_vals) + np.mean(X_vals), points_number)

y1 = ss.norm(loc=mu, scale=sigma)
y2 = ss.expon(scale=Lambda)
y3 = ss.uniform(loc=a, scale=b - a)

yCDF1 = y1.cdf(xCDF)
yCDF2 = y2.cdf(xCDF)
yCDF3 = y3.cdf(xCDF)

plt.plot(x, y, drawstyle='steps-post')
plt.plot(xCDF, yCDF1)
plt.plot(xCDF, yCDF2)
plt.plot(xCDF, yCDF3)

plt.legend(["Эмпирическая функция распределения исходного набора данных",
            f"Функция распределения N(5, 10) с отклонением Q={error_Q(x, y, y1)}",
            f"Функция распределения Exp(5) с отклонением Q={error_Q(x, y, y2)}",
            f"Функция распределения U[1, 12] с отклонением Q={error_Q(x, y, y3)}"], loc='lower right')
plt.show()
