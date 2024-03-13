import numpy as np

X = np.array([95, 86, 98])
Y = np.array([100, 90, 78])

c = (X - X.mean()) @ (Y - Y.mean()) / (len(X) - 1)
print(c)

cov = np.array([
    [np.var(X, ddof=1), c],
    [c, np.var(Y, ddof=1)]
])

print(cov)
