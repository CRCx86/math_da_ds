import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import requests
import io

data_url = 'https://code.s3.yandex.net/Math/datasets/lfw_people.npz'
response = requests.get(data_url)
lfw_people = np.load(io.BytesIO(response.content))

X, y = lfw_people['X'].astype(int), lfw_people['y'].astype(int)


def plot_images(X_tsne):
    fig, ax = plt.subplots(figsize=(24, 24))
    plt.xlim(X_tsne[:, 0].min() - 5, X_tsne[:, 0].max() + 5)
    plt.ylim(X_tsne[:, 1].min() - 5, X_tsne[:, 1].max() + 5)
    for (x0, y0), x, label in zip(X_tsne, lfw_people['images'].astype(np.uint8), y):
        ab = AnnotationBbox(
            OffsetImage(x),
            (x0 + np.random.randn() * 2, y0 + np.random.randn() * 2),
            frameon=True,
            pad=0.01,
            bboxprops=dict(edgecolor=['red', 'blue'][label]),
        )
        ax.add_artist(ab)
    plt.show()


eps = 1e-20
X1 = X - np.mean(X, axis=0)
X_norm = X1 / (eps + X1.std(axis=0))
X_tsne = TSNE(n_components=2, random_state=42).fit_transform(X_norm)

plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y)
plt.show()

plot_images(X_tsne)
