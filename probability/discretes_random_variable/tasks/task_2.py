from scipy import stats

# Определим параметр распределения.
mu = 7

# Зададим распределение.
X = stats.poisson(mu)

# Создадим набор значений.
x = 9

result = 1 - X.cdf(x)

print(result)
