import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-5, 8, 0.1)
y = -3 * x * x + 2 * x - 7
plt.plot(x, y)
