import numpy as np

X = np.array([
    [1, 4, 5],
    [3, 6, 2],
    [2, 10, 12],
    [3, 9, 6],
    [2, 5, 0],
    [0, 8, 3],
    [1, 8, 9],
    [1, 6, 2],
    [2, 8, 10],
    [0, 5, 7],
])

x = X[:, 0]
y = X[:, 1]
z = X[:, 2]

cov = (x - x.mean()) @ (y - y.mean()) / (len(X) - 1)
cov_xz = (x - x.mean()) @ (z - z.mean()) / (len(X) - 1)
cov_yz = (y - y.mean()) @ (z - z.mean()) / (len(X) - 1)

cov_mat = np.array([
    [np.var(x, ddof=1), cov, cov_xz],
    [cov, np.var(y, ddof=1), cov_yz],
    [cov_xz, cov_yz, np.var(z, ddof=1)],
])

print(cov_mat)
