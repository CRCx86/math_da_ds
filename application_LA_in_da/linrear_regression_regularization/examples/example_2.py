import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# В первом столбце число часов с начала рабочего дня,
# во втором — температура на улице.
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

X_new = np.array([[2.8, 13.2],
                  [4., 12.]])

y_new = np.array([81.5, 71.5])

y_new_pred = model.predict(X_new)
print(f"Ошибка линейной регрессии на новых данных: {mean_squared_error(y_new_pred, y_new)}")

y_pred_const = np.ones(len(y_new)) * y.mean()
print(f"Ошибка константного предсказания на новых данных: {mean_squared_error(y_pred_const, y_new)}")
