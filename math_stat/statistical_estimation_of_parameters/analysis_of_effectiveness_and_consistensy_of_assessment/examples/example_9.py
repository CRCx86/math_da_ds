import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Шаг 1: Допущение
X = np.random.normal(17, 20, 10000)  # Мы этого не знаем, это секрет, тссссс

# Шаг 2: Строим гистограмму
plt.hist(X)
plt.show()

# Шаг 3: Оцениваем мат.ожидание и дисперсию
# Мат.ожидание - используем выборочное среднее, см. уроки 1-2 темы 2 Стат.Методы
# Дисперсия - с помощью смещённой оценки дисперсии, см. там же
Mean = np.mean(X)
Var = np.var(X)
print(Mean, Var)

# Шаг 4: построим на одном графике гистограмму исходного набора данных
# и функцию плотности распределения с учётом оценённых значений параметров.
plt.hist(X, density=True, bins=30)

x_axis = np.arange(Mean - 4 * np.sqrt(Var), Mean + 4 * np.sqrt(Var), 0.01)  # ось Х
plt.plot(x_axis, norm.pdf(x_axis, Mean, np.sqrt(Var)))  # второй параметр - вероятность нормального распределения?
plt.show()
