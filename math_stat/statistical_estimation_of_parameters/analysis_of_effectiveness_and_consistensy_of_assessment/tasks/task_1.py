import numpy as np

mu = 0
sigma2 = 4
repeat_num = 100
theta = []

for i in range(repeat_num):
    X = np.random.normal(mu, np.sqrt(sigma2), 10)
    theta.append(np.var(X, ddof=1))

# print(theta)

MSE = 0

# Ваш код здесь
MSE = np.mean((np.array(theta) - sigma2) ** 2)

print("MSE данного набора оценок равна:", MSE)
