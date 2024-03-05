import numpy as np
import matplotlib.pyplot as plt

mu = 5
sigma2 = 10
repeat_num = 40
i = 2

theta1 = []
theta2 = []

while i < repeat_num:
    diff1 = []
    diff2 = []
    i = i + 1
    for j in range(1000):
        X = np.random.normal(mu, np.sqrt(sigma2), i)
        E1 = np.var(X)
        E2 = np.var(X, ddof=1)
        diff1.append((E1 - sigma2) ** 2)
        diff2.append((E2 - sigma2) ** 2)
    theta1.append(np.mean(diff1))
    theta2.append(np.mean(diff2))

plt.scatter(range(2, i), theta1)
plt.scatter(range(2, i), theta2)
plt.legend(["Смещённая оценка дисперсии", "Несмещённая оценка дисперсии"])
plt.xlabel("Число итераций")
plt.ylabel("MSE")
plt.show()
