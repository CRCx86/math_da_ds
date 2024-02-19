from scipy import stats

# Зададим распределение.
X = stats.geom(4 / 52)

# Создадим набор значений.
x = 10

result = X.cdf(x)

print(result)
