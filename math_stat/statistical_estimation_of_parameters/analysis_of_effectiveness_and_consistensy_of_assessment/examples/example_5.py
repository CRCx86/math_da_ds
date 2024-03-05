import numpy as np
import matplotlib.pyplot as plt

a = 5
b = 10
i = 2
repeat_num = 40

theta1 = []
theta2 = []

while i < repeat_num:
    diff1 = []
    diff2 = []
    i = i + 1
    for j in range(100):
        X = np.random.uniform(a, b, i)
        E1 = np.mean(X)
        E2 = np.median(X)
        diff1.append((E1-(a+b)/2)**2)
        diff2.append((E2-(a+b)/2)**2)
    theta1.append(np.mean(diff1))
    theta2.append(np.mean(diff2))

plt.scatter(range(2, i), theta1)
plt.scatter(range(2, i), theta2)
plt.legend(["Выборочное среднее", "Медиана"])
plt.xlabel("Число итераций")
plt.ylabel("MSE")
plt.show()