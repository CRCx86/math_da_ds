from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt

X, y = load_digits(return_X_y=True)
eps = 1e-6
points = PCA(2).fit_transform(X / (eps + X.std(0)))
plt.scatter(points[:, 0], points[:, 1], cmap='rainbow', c=y)
plt.show()

print(X[0])
print(X.std(0))
print(X[0] / (1e-6 + X.std(0)))
