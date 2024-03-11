import numpy as np

x = np.array([16, 10, 21, 22, 6, 17, 19, 14, 19])

mean = np.mean(x)
std = np.std(x, ddof=1)

# print(mean)
# print(std)

print(mean - 1.85938 * std/np.sqrt(len(x)))
print(mean + 1.85938 * std/np.sqrt(len(x)))
