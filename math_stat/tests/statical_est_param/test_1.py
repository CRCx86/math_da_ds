import numpy as np
from matplotlib import pyplot as plt

X = np.random.binomial(10, 1 / 4, 10000)

plt.hist(X)
plt.show()
