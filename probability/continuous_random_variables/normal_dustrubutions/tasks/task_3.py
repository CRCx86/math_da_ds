from scipy.stats import norm

mu = 35
sigma = 2.2

x = 50

X = norm(loc=mu, scale=sigma)

result = 1 - X.cdf(x=x)  # Переменная для значения вероятности
print(result)
