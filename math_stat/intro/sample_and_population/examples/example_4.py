import numpy as np
from matplotlib import pyplot as plt

x = np.random.binomial(1000, 0.5, 10000)

# Построим список интервалов по 20 значений.
bins = np.arange(420, 570, 20)  # [420, 440, ..., 540, 560]

plt.hist(x, bins=bins, weights=np.ones_like(x) / len(x))
plt.show()
