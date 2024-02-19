from scipy import stats

# Здесь ваш код.
X = stats.geom(0.2)

x = 5

result = X.pmf(x)

print(result)  # Сохраните полученную вероятность в переменной result.
