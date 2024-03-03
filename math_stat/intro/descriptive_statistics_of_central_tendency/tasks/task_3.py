import numpy as np
from scipy import stats

x = np.array([1, 2, 4, 3, 1, 5, 4, 3, 3, 1, 2, 4, 2, 3, 2, 4, 2, 2, 5, 4])

# Здесь ваш код.
result = stats.mode(x).mode

print(result.mode[0])
