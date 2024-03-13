import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

data_url = 'https://code.s3.yandex.net/Math/datasets/phone_prices_ru.csv'
data = pd.read_csv(data_url)
print(data.columns)
X = data.iloc[:, 2:-1].values
y = data.iloc[:, -1].values

# random_state необходимо зафиксировать,
# чтобы при каждом запуске разбиение было одинаковым.
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

n_components = 1
pca = PCA(X.shape[1], random_state=42).fit(X_train / X_train.std(0))

plt.bar(range(1, X.shape[1] + 1), pca.singular_values_)

error = 3561
error_n = 3560
while error > error_n and n_components < X.shape[1]:
    pca = PCA(n_components, random_state=42).fit(X_train / X_train.std(0))
    lr = LinearRegression().fit(pca.fit_transform(X_train / X_train.std(0)), y_train)
    error = mean_absolute_error(y_test, lr.predict(pca.transform(X_test / X_train.std(0))))
    if error < error_n:
        break
    print(f"Средняя ошибка при {n_components} компонентах: {error:.4f} баллов")
    n_components += 1

print(f"Средняя ошибка при {n_components} компонентах: {error:.4f} баллов")

# Простая визуализация.
plt.show()
