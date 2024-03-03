import numpy as np

# Самостоятельно зададим выборку.
x = np.array([1, 2, 3, 4, 5, 100])

median_value = np.median(x)
mean_value = np.mean(x)

print(median_value)  # -> 3.5
print(mean_value)  # -> 19.166666666666668
