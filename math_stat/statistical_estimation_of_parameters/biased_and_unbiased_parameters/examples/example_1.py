import numpy as np
import matplotlib.pyplot as plt

a = 5  # параметры распределения
b = 10
i = 0
repeat_num = 50  # максимальный размер выборки

theta = []  # массив средних значений оценок

while i < repeat_num:
    diff = []
    i = i + 1
    for j in range(100):
        X = np.random.uniform(a, b, i)
        E1 = np.mean(X) + i
        diff.append(E1)
    theta.append(np.mean(diff))

plt.scatter(range(i), theta)
plt.show()
