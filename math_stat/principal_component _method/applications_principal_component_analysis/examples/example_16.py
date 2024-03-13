from sklearn.manifold import TSNE
from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt

X, y = load_digits(return_X_y=True)

points = TSNE(2).fit_transform(X)
plt.scatter(points[:, 0], points[:, 1], cmap='rainbow', c=y)
plt.show()
