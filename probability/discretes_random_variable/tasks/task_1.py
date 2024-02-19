from scipy import stats

# Здесь ваш код.

# Определим параметр распределения.
mu = 7

# Зададим распределение.
X = stats.poisson(mu)

# Создадим набор значений.
x = 9

result = X.pmf(x)

print(result)  # Сохраните вероятность в переменную result.
