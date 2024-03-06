import numpy as np
from scipy.stats import norm

size = 100
X = np.random.normal(8, 3, size)

mu1 = 7
mu2 = 12
sigma1 = 6
sigma2 = 2

Prob_theta11 = 1
Prob_theta12 = 1
Prob_theta21 = 1
Prob_theta22 = 1

# Здесь ваш код
for i in X:
    Prob_theta11 *= norm.pdf(x=i, loc=mu1, scale=sigma1)
    Prob_theta12 *= norm.pdf(x=i, loc=mu1, scale=sigma2)
    Prob_theta21 *= norm.pdf(x=i, loc=mu2, scale=sigma1)
    Prob_theta22 *= norm.pdf(x=i, loc=mu2, scale=sigma2)

if Prob_theta11 == max(Prob_theta11, Prob_theta21, Prob_theta12, Prob_theta22):
    print("Наилучшие оценки это: первая оценка математического ожидания и первая оценка дисперсии")
if Prob_theta12 == max(Prob_theta11, Prob_theta21, Prob_theta12, Prob_theta22):
    print("Наилучшие оценки это: первая оценка математического ожидания и вторая оценка дисперсии")
if Prob_theta21 == max(Prob_theta11, Prob_theta21, Prob_theta12, Prob_theta22):
    print("Наилучшие оценки это: вторая оценка математического ожидания и первая оценка дисперсии")
if Prob_theta22 == max(Prob_theta11, Prob_theta21, Prob_theta12, Prob_theta22):
    print("Наилучшие оценки это: вторая оценка математического ожидания и вторая оценка дисперсии")
