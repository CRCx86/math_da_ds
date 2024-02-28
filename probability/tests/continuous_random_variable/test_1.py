from scipy.stats import expon

Lambda = 1 / 3
Scale = 1 / Lambda
x1 = 5
x2 = 5.25

prev = expon.cdf(x=x1, scale=Scale)
next = expon.cdf(x=x2, scale=Scale)

result = next - prev
print(result)
