import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.decomposition import PCA

X, y = load_diabetes(return_X_y=True)

# random_state необходимо зафиксировать,
# чтобы при каждом запуске разбиение было одинаковым.
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Уменьшаем размерность данных с 10 столбцов до 4.
pca = PCA(4, random_state=42)
lr = LinearRegression().fit(pca.fit_transform(X_train / X_train.std(0)), y_train)

error = mean_absolute_error(y_test, lr.predict(pca.transform(X_test / X_train.std(0))))
print(f"Средняя ошибка линейной регрессии: {error:.4f} баллов")

const_error = mean_absolute_error(y_test, np.ones(len(y_test)) * y_train.mean())
print(f"Средняя ошибка константного предикта: {const_error:.4f} баллов")
