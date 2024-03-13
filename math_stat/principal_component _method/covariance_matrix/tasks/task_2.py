import numpy as np

X = np.array([28, 17, 34, 15, 10])
Y = np.array([40, 24, 42, 18, 5])

c = (X - X.mean()) @ (Y - Y.mean()) / (len(X) - 1)

cov = np.array([
    [np.var(X, ddof=1), c],
    [c, np.var(Y, ddof=1)]
])

print(cov)
