import numpy as np
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

X, y = load_wine(return_X_y=True)
X_norm = X / X.std(axis=0)
points = PCA(2).fit_transform(X_norm)
plt.scatter(points[:, 0], points[:, 1])
plt.show()