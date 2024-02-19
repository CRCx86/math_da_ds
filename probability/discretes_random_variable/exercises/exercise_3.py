from scipy import stats
import numpy as np

# Здесь ваш код.

# Определим параметр распределения.
mu = 2.5

# Зададим распределение.
X = stats.poisson(mu)

# Создадим набор значений.
x = np.array([0, 1, 2, 3, 4])

result = X.pmf(x)

print(result)  # Сохраните полученный ответ в переменную result.
