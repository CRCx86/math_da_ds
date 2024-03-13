from scipy import stats
import numpy as np

# T = stats.t(df=100)
# t_025 = T.ppf(q=1 - 0.025)
# t_05 = T.ppf(q=0.025)
#
# print(t_05) # слева
# print(t_025) # справа

# T = stats.t(df=133)
# tt = 2*(1 - T.cdf(2.8))
# print(tt)

# # задача 2. урок 4. Тесты для среднего
# Z = stats.norm(loc=0, scale=1)
# z_2 = 2 * (1 - Z.cdf(x=2))
# print(z_2)

# задача 3 урок 4. Тесты для среднего
# T = stats.t(df=133)
# t = T.ppf(q=1 - 0.05)
# print(t)

# Упр 2 урок 5 A/B тестирование
# T = stats.t(df=198)
# t = T.ppf(q=0.05)
# print(t)

# Z = stats.norm(loc=0, scale=1)
# z_2 = 2 * (1 - Z.cdf(x=1.03))
# print(z_2)

# контрольная, тема 3, задача 1
x = 6
mu = 5
sigma = 2
n = 16

z = (x - mu) / (sigma / np.sqrt(n))

# X = stats.norm(loc=0, scale=1)
# result = 1-X.cdf(x=z)

X = stats.norm(loc=mu, scale=sigma/np.sqrt(n))
result = 1-X.cdf(x=x)
print(result)
