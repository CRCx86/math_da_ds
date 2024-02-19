from scipy import stats

# Здесь ваш код.

mu = 20

X = stats.poisson(mu)

result_1 = X.cdf(15)
result_2 = X.cdf(30) - X.cdf(15)
result_3 = 1 - X.cdf(30)

print(result_1)
print(result_2)
print(result_3)
