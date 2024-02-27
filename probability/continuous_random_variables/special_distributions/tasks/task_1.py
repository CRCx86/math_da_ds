from scipy.stats import uniform

a = 0
b = 10

x = 9

result = 1 - uniform.cdf(x=x, loc=a, scale=b)

print(result)
