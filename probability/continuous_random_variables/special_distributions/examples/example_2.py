# Подключение необходимой библиотеки.
from scipy.stats import expon

Lambda = 1 / 45  # Параметр Lambda.
Scale = 1 / Lambda  # Дополнительная величина, равная среднему исходного распределения.
x = 120  # Точка, в которой мы хотим посчитать вероятность функции распределения.
print(1 - expon.cdf(x=x, scale=Scale))  # Вывод вероятности правее точки x.
