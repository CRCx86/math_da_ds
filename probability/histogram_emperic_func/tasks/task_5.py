import numpy as np
from scipy import stats

# Введите код здесь
Lambda = 3
n_size = 50

X = stats.expon(scale=Lambda)
Sample_X = X.rvs(n_size)

mean = np.mean(Sample_X)
print(mean)

var = np.var(Sample_X)
print(var)

std = np.std(Sample_X)
print(std)
