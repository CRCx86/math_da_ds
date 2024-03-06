import numpy as np
import matplotlib.pyplot as plt

size = 1000
k1 = 0.5
mu1 = 0
sigma1 = 10
mu2 = 100
sigma2 = 20
X = np.concatenate((np.random.normal(mu1, sigma1, int(k1 * size)), np.random.normal(mu2, sigma2, int((1 - k1) * size))),
                   axis=0)
plt.hist(X, density=True, bins=30)
plt.show()
