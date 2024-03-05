import numpy as np
import matplotlib.pyplot as plt

a = 5
b = 10
i = 2
repeat_num = 40

true_var = (b - a) ** 2 / 12

theta1 = []
theta2 = []

while i < repeat_num:
    diff1 = []
    diff2 = []
    i = i + 1
    for j in range(100):
        X = np.random.uniform(a, b, i)
        E1 = np.var(X)
        E2 = np.var(X, ddof=1)
        diff1.append((E1 - true_var) ** 2)
        diff2.append((E2 - true_var) ** 2)
    theta1.append(np.mean(diff1))
    theta2.append(np.mean(diff2))

plt.scatter(range(2, i), theta1)
plt.scatter(range(2, i), theta2)
plt.legend(["MSE смещённой оценки дисперсии", "MSE несмещённой оценки дисперсии"])
plt.xlabel("Число итераций")
plt.ylabel("MSE")
plt.show()
