import numpy as np
from matplotlib import pyplot as plt

x = np.random.binomial(1000, 0.5, 10000)

val, cnt = np.unique(x, return_counts=True)
pmf = cnt / len(x)

plt.bar(val, pmf)
plt.show()
