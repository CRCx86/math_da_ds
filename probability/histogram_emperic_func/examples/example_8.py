import matplotlib.pyplot as plt
import scipy.stats as ss
import numpy as np

# Параметр экспоненциального распределения
Lambda = 5
# Длина столбцов гистограммы
bin_length = 0.005
# Размер выборки
n_size = 1000000

X = ss.expon(scale=1 / Lambda)
X_vals = X.rvs(n_size)
# Количество точек, в которых будем строить функцию плотности
points_number = 1000
# Создаём точки по оси x для изображения функции плотности
x_points_pdf = np.linspace(X_vals.min(), X_vals.max(), points_number)
# Создаём точки по оси y для изображения функции плотности
y_points_pdf = X.pdf(x_points_pdf)

# Рассчитываем число столбцов как общая длина графика по оси x,
# делённая на ширину каждого столбца
bins_number = int((X_vals.max() - X_vals.min()) // bin_length)

# Строим гистограмму и график плотности
plt.hist(X_vals, density=True, bins=bins_number)
plt.title("Плотность и гистограмма при размере выборки " + str(n_size) + " и ширине столбцов " + str(bin_length))
plt.plot(x_points_pdf, y_points_pdf)
plt.show()
