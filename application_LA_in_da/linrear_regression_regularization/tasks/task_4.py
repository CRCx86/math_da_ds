import numpy as np
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# Не забудьте импортировать все необходимые инструменты

X = np.genfromtxt('https://code.s3.yandex.net/Math/datasets/X.csv', delimiter=',')
y = np.genfromtxt('https://code.s3.yandex.net/Math/datasets/y.csv', delimiter=',')
X_test = np.genfromtxt('https://code.s3.yandex.net/Math/datasets/X_test.csv', delimiter=',')
y_test = np.genfromtxt('https://code.s3.yandex.net/Math/datasets/y_test.csv', delimiter=',')

# ridge_model = Ridge(alpha=1)
# ridge_model_fit = ridge_model.fit(X, y)

# alpha = 1
# while alpha < 100:
#     model = Ridge(alpha=alpha)  # Выбираем модель
#     model.fit(X, y)  # Коэффициенты регрессии подбираются под данные
#     print(f"alpha: {alpha}. Ошибка модели на новых данных: {mean_squared_error(model.predict(X_test), y_test)}")
#     print(f"Коэффициенты модели: {model.coef_}")
#     print()
#     alpha = alpha + 1

alpha = 1
while alpha < 100:
    model = Lasso(alpha=alpha)  # Выбираем модель
    model.fit(X, y)  # Коэффициенты регрессии подбираются под данные
    print(f"alpha: {alpha}. Ошибка модели на новых данных: {mean_squared_error(model.predict(X_test), y_test)}")
    print(f"Коэффициенты модели: {model.coef_}")
    print()
    alpha = alpha + 1
