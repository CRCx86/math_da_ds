import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

mu_1 = 15
mu_2 = 20

sigma_1 = 10
sigma_2 = 10

n = 100

X = np.random.lognormal(mu_1, sigma_1, n)
Y = np.random.lognormal(mu_2, sigma_2, n)

pvalue = 0  # Переменная для сохранения p-value.

# Ваш код здесь.
LogX = np.log(X)
LogY = np.log(Y)

pvalue = stats.ttest_ind(a=LogX, b=LogY, equal_var=True)[1]
print("pvalue", pvalue)

if pvalue < 0.05:
    print("Выборки обладают различными средними.")
else:
    print("Выборки могут обладать одинаковыми средними.")
