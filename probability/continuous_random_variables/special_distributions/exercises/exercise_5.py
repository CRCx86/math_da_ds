# Подключение необходимой библиотеки.
from scipy.stats import uniform

a = 0
b = 180

x = 30

result = 1 - uniform.cdf(x=x, loc=a, scale=b)

print(result)
