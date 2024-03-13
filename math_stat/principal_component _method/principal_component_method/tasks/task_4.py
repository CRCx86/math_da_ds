import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

data_url = 'https://code.s3.yandex.net/Math/datasets/zoo_ru.csv'
full_data = pd.read_csv(data_url)
names = full_data.values[:, 0]
data = full_data.values[:, 1:-1].astype(float)
classes = full_data.values[:, -1].astype(int)


def scatter_texts(points, texts, colors=None):
    # Код выводит scatter-график с текстами вместо точек.
    # Пример использования: `scatter_texts(points, names, classes)`

    i = 0

    while i < len(points):
        color = 'C0' if colors is None else plt.cm.tab10_r(colors[i] / colors.max())

        plt.text(
            points[i, 0] + np.random.randn() / 2.5,
            points[i, 1] + np.random.randn() / 2.5,
            texts[i],
            c=color
        )

        i += 1

        plt.xlim(points[:, 0].min() - 1, points[:, 0].max() + 1)
        plt.ylim(points[:, 1].min() - 1, points[:, 1].max() + 1)


# Ваш код
# это всё про похожесть объектов, заданных матрицей
data_centered = data - data.mean(axis=0)
U, S, Vt = np.linalg.svd(data_centered)

n_components = 2
data_compressed = data_centered @ Vt.T[:, 0:n_components]

print(data_compressed)

scatter_texts(data_compressed, names, classes)

plt.show()
