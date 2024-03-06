import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.stats import norm

size = 1000
k1 = 0.5
mu1 = 0
sigma1 = 10
mu2 = 100
sigma2 = 20
X = np.concatenate((np.random.normal(mu1, sigma1, int(k1 * size)), np.random.normal(mu2, sigma2, int((1 - k1) * size))),
                   axis=0)


def normal_mixture(params):
    omega, mu1, sigma1, mu2, sigma2 = params
    s = 0

    i = 0
    while (i < len(X)):
        s = s + np.log(
            float(
                omega / (sigma1 * np.sqrt(2 * np.pi)) * np.exp(-0.5 * (X[i] - mu1) ** 2 / sigma1 ** 2)
                + (1 - omega) / (sigma2 * np.sqrt(2 * np.pi)) * np.exp(-0.5 * (X[i] - mu2) ** 2 / sigma2 ** 2)
            )
        )
        i = i + 1

    return -s


def opt():
    x0 = np.array([0.5, 0, 50, 200, 100])
    return minimize(normal_mixture, x0, tol=1e-3, method='Nelder-Mead')


estimate_parameters = opt().x
omega = estimate_parameters[0]
mu1 = estimate_parameters[1]
sigma1 = estimate_parameters[2]
mu2 = estimate_parameters[3]
sigma2 = estimate_parameters[4]

plt.hist(X, density=True, bins=40)
x_axis = np.arange(mu1 - 4 * sigma1, mu2 + 4 * sigma2, 0.01)
plt.plot(x_axis, omega * norm.pdf(x_axis, mu1, sigma1) + (1 - omega) * norm.pdf(x_axis, mu2, sigma2))
plt.show()
