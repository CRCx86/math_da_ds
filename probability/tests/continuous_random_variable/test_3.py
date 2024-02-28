# Подключение необходимой библиотеки.
from scipy.stats import norm

mu = 3000
sigma = 600

x = 3200

X = norm(loc=mu, scale=sigma)

result = X.cdf(x=x)
print(result)
