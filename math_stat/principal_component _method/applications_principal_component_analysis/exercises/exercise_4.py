import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA


# Строит plt.scatter со словами вместо точек.
def scatter_texts(points, texts, labels=None):
    i = 0
    points = np.copy(points) + np.random.randn(len(points), 2) * points.std(0) / 5
    plt.figure(figsize=(12, 8))
    while i < len(X):
        color = 'C0' if labels is None else plt.cm.tab10_r(labels[i] / labels.max())
        plt.text(
            points[i, 0],
            points[i, 1],
            texts[i],
            c=color
        )
        i += 1
    plt.xlim(points[:, 0].min(), points[:, 0].max())
    plt.ylim(points[:, 1].min(), points[:, 1].max())
    plt.show()


full_data = pd.read_csv('https://code.s3.yandex.net/Math/datasets/zoo.csv')
X = full_data.values[:, 1:-1].astype(float)
y = full_data.values[:, -1].astype(int)
animal_names = full_data['animal_name']

eps = 1e-6
points = PCA(2).fit_transform(X)
scatter_texts(points, animal_names, y)

points = TSNE(2).fit_transform(X)
scatter_texts(points, animal_names, y)
