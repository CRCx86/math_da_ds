import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error

# Не забудьте импортировать все необходимые инструменты

X = np.genfromtxt('https://code.s3.yandex.net/Math/datasets/X.csv', delimiter=',')
y = np.genfromtxt('https://code.s3.yandex.net/Math/datasets/y.csv', delimiter=',')
X_test = np.genfromtxt('https://code.s3.yandex.net/Math/datasets/X_test.csv', delimiter=',')
y_test = np.genfromtxt('https://code.s3.yandex.net/Math/datasets/y_test.csv', delimiter=',')

linear_model = LinearRegression()
linear_model.fit(X, y)

print(f"Ошибка линейной регрессии: {mean_squared_error(linear_model.predict(X), y)}")
print(f"Ошибка модели на новых данных: {mean_squared_error(linear_model.predict(X_test), y_test)}")
print(f"Коэффициенты регрессии: {linear_model.coef_}")
print(f"Cвободный член: {linear_model.intercept_}")

ridge_model = Ridge(alpha=1)
ridge_model_fit = ridge_model.fit(X, y)

print()
print(f"Ошибка Ridge регрессии: {mean_squared_error(ridge_model.predict(X), y)}")
print(f"Ошибка модели на новых данных: {mean_squared_error(ridge_model.predict(X_test), y_test)}")
print(f"Коэффициенты регрессии: {ridge_model.coef_}")
print(f"Cвободный член: {ridge_model.intercept_}")

lasso_model = Lasso(alpha=1)
lasso_model_fit = lasso_model.fit(X, y)

print()
print(f"Ошибка Lasso регрессии: {mean_squared_error(lasso_model.predict(X), y)}")
print(f"Ошибка модели на новых данных: {mean_squared_error(lasso_model.predict(X_test), y_test)}")
print(f"Коэффициенты регрессии: {lasso_model.coef_}")
print(f"Cвободный член: {lasso_model.intercept_}")
