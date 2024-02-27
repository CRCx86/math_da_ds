from scipy.stats import norm

mu = 35
sigma = 2.2

x = 25

X = norm(loc=mu, scale=sigma)

result = X.cdf(x=x)  # Переменная для значения вероятности
print(result)
