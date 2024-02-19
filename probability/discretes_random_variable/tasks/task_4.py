from scipy import stats
import numpy as np

# Здесь ваш код.
# Зададим распределение.
X = stats.binom(12, 72 / 100)

# Создадим набор значений.
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

result = X.pmf(x)

print(result)  # Сохраните полученный результат в переменной result.
