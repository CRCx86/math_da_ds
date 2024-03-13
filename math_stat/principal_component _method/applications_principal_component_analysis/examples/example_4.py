import numpy as np
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

X, y = load_wine(return_X_y=True)
points = PCA(2).fit_transform(X)
plt.figure(figsize=(12, 8))
plt.scatter(points[:, 0], points[:, 1], c=((points[:, 0] > 200) & (points[:, 1] < 30)))
plt.show()
