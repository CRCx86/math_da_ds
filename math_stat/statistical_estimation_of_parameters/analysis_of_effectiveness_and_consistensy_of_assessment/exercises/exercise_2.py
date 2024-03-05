import numpy as np
import matplotlib.pyplot as plt

a = 5
b = 10
size = 100
n = 50
True_Mean = (a + b) / 2

MSE_Mean = 0
MSE_Median = 0

estim1 = []
estim2 = []

# Ваш код здесь
for i in range(n):
    X = np.random.uniform(a, b, size)
    estim1.append(np.mean(X))
    estim2.append(np.median(X))

diff1 = []
for i in estim1:
    diff1.append((i - True_Mean) ** 2)

diff2 = []
for i in estim2:
    diff2.append((i - True_Mean) ** 2)

MSE_Mean = np.mean(diff1)
MSE_Median = np.mean(diff2)

if MSE_Mean > MSE_Median:
    print("Разность между MSE:", MSE_Mean - MSE_Median)
    print("Более точная оценка по MSE: Медиана")
else:
    print("Разность между MSE:", MSE_Median - MSE_Mean)
    print("Более точная оценка по MSE: Выборочное Среднее")
