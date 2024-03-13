import numpy as np
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

X, y = load_wine(return_X_y=True)
print("исходные: ")
print(X)

X_norm = X / X.std(axis=0)

print("нормализованные: ")
print(X_norm)
pca = PCA(n_components=2)

data_compressed = pca.fit_transform(X_norm)

plt.scatter(data_compressed[:, 0], data_compressed[:, 1], c=y)
# plt.show()
