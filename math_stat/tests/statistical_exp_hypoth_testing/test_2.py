import numpy as np

# Допишите код здесь.
from scipy import stats

x = np.array([15.5, 21.0, 16.5, 19.2, 18.6, 19.1, 18.5, 19.3, 19.7,
              16.9, 18.7, 18.2, 18.0, 17.5, 19.8, 18.0, 19.8, 18.2,
              20.2, 14.5, 18.5, 20.5, 20.3, 21.8])

# Допишите код здесь.
n = len(x)
sigma = np.std(x, ddof=1)

Z = stats.t(df=n-1)
q = (1 - 0.9) / 2
z = Z.ppf(1 - q)

left = np.mean(x) - z * sigma / np.sqrt(n)
right = np.mean(x) + z * sigma / np.sqrt(n)

print(left)  # Левая граница доверительного интервала.
print(right)  # Правая граница доверительного интервала.
