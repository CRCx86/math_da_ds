import numpy as np

# Здесь ваш код.
x = np.random.geometric(0.5, 10000)

median = np.median(x)
mean = np.mean(x)

print(median)
print(mean)
