from scipy import stats

X = stats.binom(5, 1 / 3)

p = X.pmf(2)

print(p)
