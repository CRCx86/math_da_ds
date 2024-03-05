import numpy as np
import matplotlib.pyplot as plt

a = 5
b = 10
i = 2
repeat_num = 30

theta1 = []
theta2 = []

while i < repeat_num:
    diff1 = []
    diff2 = []
    i = i + 1
    for j in range(1000):
        X = np.random.uniform(a, b, i)
        E1 = np.var(X)
        E2 = np.var(X, ddof=1)
        diff1.append(E1)
        diff2.append(E2)
    theta1.append(np.mean(diff1))
    theta2.append(np.mean(diff2))
    # diff.append(np.mean(theta) - (a + b) / 2)

plt.scatter(range(2, i), theta1)
plt.scatter(range(2, i), theta2)
plt.legend(["Смещённая оценка", "Несмещённая оценка"])
plt.show()

plt.show()
