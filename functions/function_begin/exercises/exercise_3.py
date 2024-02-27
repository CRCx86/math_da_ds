import numpy as np
from matplotlib import pyplot as plt

caries_data = np.array([[4.4, 25.],
                        [12.4, 35.],
                        [15.5, 45.],
                        [14.8, 55.],
                        [12.4, 65.]])

percent = caries_data[:, 0]
age = caries_data[:, 1]

# Визуализируем точки данных.
plt.scatter(age, percent)

# Рассчитываем коэффициенты полинома.
# Подставили в функцию степень 1, поэтому полином линейный.
coefs = np.polyfit(age, percent, 3)
# Создаём Python-функцию для подсчёта значения полинома.
f = np.poly1d(coefs)

# Рассчитываем координаты точек для графика полинома.
x = np.arange(20, 70, 0.5)
# Находим значения найденного полинома.
y = f(x)

# Визуализируем полином.
plt.plot(x, y)

# Печатаем коэффициенты.
# print("coefs", coefs)

# Печатаем значение полинома для указанного аргумента.
caries_35 = f(35)
print(caries_35)
