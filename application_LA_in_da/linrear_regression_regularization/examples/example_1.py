import numpy as np
from sklearn.linear_model import LinearRegression
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

model = LinearRegression()  # Выбираем модель.

model.fit(X, y)  # Коэффициенты регрессии подбираются под данные.

print(f"Коэффициенты регрессии: {model.coef_}")
print(f"Cвободный член: {model.intercept_}")

y_pred = model.predict(X)
print(f"Ошибка линейной регрессии: {mean_squared_error(y_pred, y)}")

# Обратите внимание на размер созданного вектора - он такой же, как y.
y_pred_const = np.ones(len(y)) * y.mean()  # Создаём константный предикт.
print(f"Ошибка константного предсказания: {mean_squared_error(y_pred_const, y)}")
