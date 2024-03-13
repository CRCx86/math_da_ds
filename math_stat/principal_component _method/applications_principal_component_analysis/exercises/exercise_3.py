from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_url = 'https://code.s3.yandex.net/Math/datasets/credit_rus.csv'
df = pd.read_csv(data_url)
print(df.columns)
X = df.drop(['Кредитный лимит, $'], axis=1).values
y = df['Кредитный лимит, $'].values

# random_state необходимо зафиксировать,
# чтобы при каждом запуске разбиение было одинаковым.
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

n_components = 1
pca = PCA(X.shape[1], random_state=42).fit(X_train / X_train.std(0))

plt.bar(range(1, X.shape[1]+1), pca.singular_values_)

error = 701
while error > 700 and n_components < X.shape[1]:
    pca = PCA(n_components, random_state=42).fit(X_train / X_train.std(0))
    lr = LinearRegression().fit(pca.fit_transform(X_train / X_train.std(0)), y_train)
    error = mean_absolute_error(y_test, lr.predict(pca.transform(X_test / X_train.std(0))))
    if error < 700:
        break
    print(f"Средняя ошибка при {n_components} компонентах: {error:.4f} баллов")
    n_components += 1

print(f"Средняя ошибка при {n_components} компонентах: {error:.4f} баллов")

# Простая визуализация.
plt.show()
