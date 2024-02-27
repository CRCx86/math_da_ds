from scipy.stats import norm

mu = 5
sigma = 1
x = 5.5

X = norm(loc=mu, scale=sigma)

result = X.cdf(x=x)
print(result)
