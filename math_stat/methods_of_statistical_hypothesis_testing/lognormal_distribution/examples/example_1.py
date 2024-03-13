import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

X = [4.9406, 11.1565, 6.11626, 19.6103, 6.12839, 4.3416, 9.06663, 6.56027,
     5.08844, 7.23608, 9.59747, 8.27959, 6.26848, 4.80749, 6.52615,
     7.47267, 15.7362, 7.35348, 12.7505, 10.2956, 7.16994, 10.921, 12.022,
     6.47511, 12.8345, 4.76712, 5.13015, 8.11151, 4.86316, 6.70681]

plt.hist(X, density=True, bins=5)
plt.show()

# Прологарифмируем каждое значение исходной выборки

LogX = np.log(X)

plt.hist(LogX, density=True, bins=5)
plt.show()
