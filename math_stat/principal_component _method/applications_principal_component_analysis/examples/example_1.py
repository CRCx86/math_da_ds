from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [5, 12],
    [2, 5],
    [0, 2],
    [2, 10],
    [6, 25],
    [3, 14],
    [2, 12],
    [3, 23],
    [7, 26],
    [2, 16]
])

pca = PCA(n_components=1)

data_compressed = pca.fit_transform(data)
print(data_compressed)
