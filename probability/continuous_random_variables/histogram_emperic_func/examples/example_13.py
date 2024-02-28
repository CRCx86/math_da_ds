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

x, y = ecdf(X_vals)
x, y = adding(x, y, X_vals)

plt.plot(x, y, drawstyle='steps-post')
plt.legend(["Эмпирическая функция распределения"], loc='upper left')
plt.show()
