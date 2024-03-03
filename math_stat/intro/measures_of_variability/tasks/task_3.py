import numpy as np
from scipy import stats

x = np.random.poisson(10, 100000)

range_value = np.max(x) - np.min(x)
iqr_value = stats.iqr(x)

print(range_value)
print(iqr_value)
