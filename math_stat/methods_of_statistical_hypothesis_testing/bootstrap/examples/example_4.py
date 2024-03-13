import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss


def ecdf(a):
    x, counts = np.unique(a, return_counts=True)
    cusum = np.cumsum(counts)
    return x, cusum / cusum[-1]


def plot_ecdf(a):
    x, y = ecdf(a)

    x = np.insert(x, 0, x[0])
    y = np.insert(y, 0, 0.)

    plt.plot(x, y, drawstyle='steps-post')


# График эмпирической функции распределения
n = 200
X = np.random.normal(0, 1, n)
plot_ecdf(X)

# График истинной функции распределения
xCDF = np.linspace(min(X), max(X), 50)
yCDF = ss.norm.cdf(xCDF)
plt.plot(xCDF, yCDF)
plt.show()
