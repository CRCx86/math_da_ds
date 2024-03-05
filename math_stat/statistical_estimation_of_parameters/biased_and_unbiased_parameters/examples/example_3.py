import numpy as np
import matplotlib.pyplot as plt

a = 5  # Параметры распределения
b = 10
i = 0
repeat_num = 50  # Максимальный размер выборки

theta = []  # Массив средних значений оценок

while i < repeat_num:
    diff = []
    i = i + 1
    for j in range(100):
        X = np.random.uniform(a, b, i)
        E1 = np.var(X)
        diff.append(E1)
    theta.append(np.mean(diff))

plt.scatter(range(i), theta)
plt.show()
