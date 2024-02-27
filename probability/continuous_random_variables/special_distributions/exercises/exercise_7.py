# Подключение необходимой библиотеки.
from scipy.stats import expon

Lambda = 1 / 45
Scale = 1 / Lambda

x = 600

result = 1 - expon.cdf(x=x, scale=Scale)

print(result)
