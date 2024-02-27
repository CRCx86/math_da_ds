import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss

X_vals = [2.64, 8.50, 5.40, 2.54, 3.98, 3.49, 8.68, 1.08,
          3.40, 1.81, 9.41, 4.92, 5.865, 1.31, 12.15, 4.50,
          2.20, 1.16, 8.85, 8.57]

# Параметры равномерного распределения
a = 1
b = 12

# Параметр экспоненциального распределения
Lambda = 0.2

# Параметры нормального распределения
mu = 5
sigma = np.sqrt(10)

# Количество точек, в которых будем строить функцию плотности
points_number = 100
# Далее вызовем функцию гистограммы от массива X с параметром bins

bins = 8

plt.hist(X_vals, density=True, bins=bins)

# Набор точек-аргументов для изображения графиков
xPDF = np.linspace(min(X_vals) - np.mean(X_vals), max(X_vals) + np.mean(X_vals), points_number)

# Функции плотности распределения случайных величин
yPDF1 = ss.norm.pdf(xPDF, mu, sigma)
yPDF2 = ss.expon.pdf(xPDF, scale=1 / Lambda)
yPDF3 = ss.uniform.pdf(xPDF, loc=a, scale=b - a)

# Графики функций плотности распределения
plt.plot(xPDF, yPDF1)
plt.plot(xPDF, yPDF2)
plt.plot(xPDF, yPDF3)
plt.legend(["Плотность N(5, 10)",
            "Плотность Exp(5)",
            "Плотность U[1, 12]",
            "Гистограмма исходного набора данных"], loc='upper right')
plt.show()
