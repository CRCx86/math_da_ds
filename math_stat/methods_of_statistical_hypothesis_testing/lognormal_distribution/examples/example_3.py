import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

mu_1 = 4
mu_2 = 3.5

sigma_1 = 10
sigma_2 = 10

X = np.random.lognormal(mu_1, sigma_1, 30)
Y = np.random.lognormal(mu_2, sigma_2, 30)

LogX = np.log(X)
LogY = np.log(Y)

plt.hist(LogX, bins=5)
plt.hist(LogY, bins=5)
plt.show()

pvalue = stats.ttest_ind(a=LogX, b=LogY, equal_var=True)[1]
print(pvalue)
