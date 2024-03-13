from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt

X, y = load_digits(return_X_y=True)

points = PCA(2).fit_transform(X)

# cmap='rainbow' для более подходящей палитры цветов при окрашивании точек.
plt.scatter(points[:, 0], points[:, 1], cmap='rainbow', c=y)
plt.show()
