import numpy as np
from matplotlib import pyplot as plt

# Ваш код здесь.
x = np.random.geometric(1 / 2, 100000)

plt.hist(x, weights=np.ones_like(x) / len(x))
plt.show()
