import numpy as np

X = [9.96766, 2.38226, 6.99831, -6.67306, 5.30532,
     -9.5352, -4.04991, -1.18316, 1.15991, -6.5992]

print("Среднее выборки:")
print(np.mean(X))

print("Дисперсия выборки:")
print(np.var(X))

print("Стандартное отклонение выборки:")
print(np.std(X))

print("Разность максимального и минимального значений выборки:")
print(np.max(X) - np.min(X))
