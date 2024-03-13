import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import io
import requests

response = requests.get('https://code.s3.yandex.net/Math/datasets/kinopoisk_term_occurence.npy')
X = np.load(io.BytesIO(response.content), allow_pickle=True).T
df = pd.read_csv('https://code.s3.yandex.net/Math/datasets/kinopoisk-top250.csv')

# NumPy-массивы с названиями и описаниями фильмов.
names = df.movie.values
overviews = df.overview.values


# Возвращает булевый массив длины len(names).
# True ставится, если строка `phrase` встретилась в названии
# или описании соответствующего фильма.
def phrase_in_film_mask(phrase):
    i = 0
    result = np.full(len(names), False)
    while i < len(names):
        if phrase in names[i].lower() or phrase in overviews[i].lower():
            result[i] = True
        i += 1
    return result


# Пример использования для выделения фильмов на графике.
# mask = phrase_in_film_mask('властелин')
# plt.scatter(points[:, 0], points[:, 1], c=mask, cmap='rainbow')


# Ваш код.
# Создаём объект PCA
pca = PCA(n_components=2, random_state=42)

# Сжимаем данные.
X_norm = X / X.std(axis=0)
points = pca.fit_transform(X_norm)

mask = phrase_in_film_mask('пират')

plt.scatter(points[:, 0], points[:, 1], c=mask, cmap='rainbow')
plt.show()
