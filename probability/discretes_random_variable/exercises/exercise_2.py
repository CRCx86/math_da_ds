from scipy import stats

# Здесь ваш код.

X = stats.geom(1 / 1000)

result = 1 - X.cdf(500)

print(result)
