from scipy.stats import norm

mu = 35
sigma = 2.2

x1 = 25
x2 = 50

X = norm(loc=mu, scale=sigma)

result = X.cdf(x=x2) - X.cdf(x=x1)  # Переменная для значения вероятности
print(result)
