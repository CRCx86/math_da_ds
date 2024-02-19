from scipy import stats

mu = 4

X = stats.poisson(mu)

x = 10

# Введите код здесь.

result = 1 - X.cdf(x)

print(result)  # Сохраните полученную вероятность в переменной result.
