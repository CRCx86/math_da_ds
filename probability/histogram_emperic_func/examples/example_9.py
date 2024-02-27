import matplotlib.pyplot as plt
import scipy.stats as ss
import numpy as np

# Параметр распределения Бернулли
Prob = 0.2
# Ширина столбцов гистограммы
bin_length = 0.01
# Размер выборки
n_size = 10000

# Создаём выборку распределения Бернулли
X = ss.bernoulli(p=Prob)
X_vals = X.rvs(n_size)

# Рассчитываем число столбцов как общая длина графика по оси x,
# делённая на длину каждого столбца
bins_number = int((X_vals.max() - X_vals.min()) // bin_length)

# Подготовим место для двух графиков
fig, axes = plt.subplots(1, 2)

# Вызываем функцию гистограммы от массива X_vals с параметром bins и density
axes[0].hist(X_vals, density=True, bins=bins_number)
# Добавление названия к графику
axes[0].set_title(f"Длина столбцов {bin_length}")

# Вызываем функцию гистограммы от массива X_vals без параметра bins
axes[1].hist(X_vals, density=True, bins=bins_number * 2)
# Добавление названия к графику
axes[1].set_title(f"Длина столбцов {bin_length / 2}")

# Выводим оба графика
plt.show()
