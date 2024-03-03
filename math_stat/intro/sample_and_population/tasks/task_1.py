import numpy as np
from matplotlib import pyplot as plt

sec = np.array([22, 17, 27, 19, 29, 19, 19, 18, 24, 25, 18, 21, 25, 20, 15, 24, 26, 19, 28, 23])

# Здесь ваш код.
val, cnt = np.unique(sec, return_counts=True)
pmf = cnt / len(sec)

plt.bar(val, pmf)
plt.show()
