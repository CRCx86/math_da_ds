import numpy as np
from scipy import stats

n = 16
sigma = 5

Z = stats.norm(loc=0, scale=1)

alpha = (1 - 0.95) / 2
z = Z.ppf(q=1 - alpha)
print("z:", z)

left = 453 - z * sigma / np.sqrt(n)
right = 453 + z * sigma / np.sqrt(n)

print(left)  # Печатаем левую границу.
print(right)  # Печатаем правую границу.
