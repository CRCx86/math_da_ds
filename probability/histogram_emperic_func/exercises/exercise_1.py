from scipy import stats
import numpy as np

n_size = 5

# Параметры для равномерного распределения.
a = -10
b = 10

# Параметр для экспоненциального распределения.
Lambda = 2

# Параметры для нормального распределения.
mu = 2
sigma = np.sqrt(20)

# Напишите ваш код здесь.
X = stats.uniform(loc=a, scale=b - a)
Sample_X = X.rvs(n_size)

Y = stats.expon(scale=1 / Lambda)
Sample_Y = Y.rvs(n_size)

Z = stats.norm(loc=mu, scale=sigma)
Sample_Z = Z.rvs(n_size)

print(Sample_X)  # Выборка из 5 значений для случайной величины X.
print(Sample_Y)  # Выборка из 5 значений для случайной величины Y.
print(Sample_Z)  # Выборка из 5 значений для случайной величины Z.
