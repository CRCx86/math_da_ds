from scipy import stats

# Введите код здесь.
X = stats.binom(50, 0.3)

result = 1 - X.cdf(19)

print(result)  # Сохраните полученную вероятность в переменной result.
