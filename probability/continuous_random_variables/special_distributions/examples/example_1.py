from scipy.stats import uniform  # Подключение необходимой библиотеки.

a = 0  # Параметр a.
b = 100  # Параметр b.
x = 30  # Точка в которой мы хотим посчитать значение функции распределения.
print(uniform.cdf(x=x, loc=a, scale=b))  # Вывод вероятности в точке x.