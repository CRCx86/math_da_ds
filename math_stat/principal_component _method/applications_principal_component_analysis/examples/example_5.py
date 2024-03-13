import numpy as np
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

X, y = load_wine(return_X_y=True)

use_columns = [4, 12]

points = PCA(2).fit_transform(X[:, use_columns])
plt.scatter(points[:, 0], points[:, 1])
plt.title('PCA по двум выбранным столбцам')

plt.figure()
points = PCA(2).fit_transform(X)
plt.scatter(points[:, 0], points[:, 1])
plt.title('PCA по всем столбцам')
plt.show()
