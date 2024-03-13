import numpy as np

# X = np.array([12, 15, 7, 10])
#
# result = np.mean(np.log10(X))
# print(result)

X1 = np.array([4, 5, 3, 10, 4])
X2 = np.array([6, 8, 2, 3, 7])

diff = X1 - X2
print(diff)

diff_abs = sorted(abs(diff))
print(diff_abs)
