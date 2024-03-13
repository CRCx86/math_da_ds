import numpy as np
import matplotlib.pyplot as plt

mu = 10
sigma = 1
i = 2
repeat_num = 100

theta1 = []
theta2 = []

while i < repeat_num:
    diff1 = []
    i = i + 1
    for j in range(100):
        X = np.log(np.random.normal(mu, sigma, i))
        E1 = np.mean(X)
        diff1.append(E1)
    theta1.append(np.mean(diff1))
    theta2.append(np.log(mu))

plt.scatter(range(2, i), theta1)
plt.scatter(range(2, i), theta2)
plt.legend(["Математическое ожидание логарифма", "Логарифм математического ожидания"])
plt.xlabel("Число итераций")
plt.show()
