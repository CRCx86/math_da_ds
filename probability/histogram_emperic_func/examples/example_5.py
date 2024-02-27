from scipy import stats
import numpy as np

# Определяем seed() для "заморозки" случайности
np.random.seed(0)

a = 1
b = 3
n_size = 10

X = stats.uniform(loc=a, scale=b - a)
Sample_X = X.rvs(n_size)

print(Sample_X)
