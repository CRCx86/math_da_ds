import numpy as np
from matplotlib import pyplot as plt

# Здесь ваш код.

x = np.random.geometric(0.01, 100000)

# Построим список интервалов по 20 значений.
bins = np.arange(0, 1000, 5)  # [420, 440, ..., 540, 560]

plt.hist(x, bins=bins, weights=np.ones_like(x) / len(x))
plt.show()
