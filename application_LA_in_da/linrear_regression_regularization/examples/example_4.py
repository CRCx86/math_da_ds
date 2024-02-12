import numpy as np
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error

# В первом столбце число часов с начала рабочего дня,
# во втором - температура на улице.
# Если пользоваться регрессией в sklearn,
# столбец единичек справа не нужен.
X = np.array([[3.2, 11.8],
              [3.5, 11.5],
              [2.2, 12.8],
              [2.7, 12.3],
              [3.1, 11.9],
              [4., 11.],
              [1.8, 13.2],
              [5.1, 9.9]])

y = np.array([72., 63., 84., 79., 72., 62., 91., 47.])

model = Lasso(alpha=1)  # Выбираем модель.

model.fit(X, y)  # Коэффициенты регрессии подбираются под данные.

model_coefs = model.coef_  # Объект model сообщает нам коэффициенты регрессии.
model_intercept = model.intercept_  # Объект model сообщает значение свободного члена.

print(f"Коэффициенты регрессии: {model_coefs}, свободный член: {model_intercept}")
print(f"Ошибка модели: {mean_squared_error(model.predict(X), y)}")

X_test = np.array([[2.8, 13.2],
                   [4., 12.]])

y_test = np.array([81.5, 71.5])

print(f"Ошибка модели на новых данных: {mean_squared_error(model.predict(X_test), y_test)}")
