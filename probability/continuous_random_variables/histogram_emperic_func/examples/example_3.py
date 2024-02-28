# Подключение необходимых библиотек
from scipy import stats
import numpy as np

# Параметры нормального распределения
mu = 5
sigma = np.sqrt(10)

# Размер выборки
n_size = 10

# Создание случайной величины необходимого типа
X = stats.norm(loc=mu, scale=sigma)

# Создание выборки случайной величины
Sample_X = X.rvs(n_size)

print(Sample_X)
