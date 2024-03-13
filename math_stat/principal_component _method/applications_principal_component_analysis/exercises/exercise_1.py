import numpy as np
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

X, y = load_wine(return_X_y=True)

pca = PCA(n_components=2)

data_compressed = pca.fit_transform(X)
print(data_compressed)

plt.scatter(data_compressed[:, 0], data_compressed[:, 1], c=y)
plt.show()
