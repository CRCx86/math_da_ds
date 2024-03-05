import numpy as np
import matplotlib.pyplot as plt

mu = 5
sigma2 = 10
i = 2
repeat_num = 100

Means = []
Vars = []

while i < repeat_num:
    diff1 = []
    diff2 = []
    i = i + 1
    for j in range(100):
        X = np.random.normal(mu, np.sqrt(sigma2), i)
        E1 = np.mean(X)
        E2 = np.var(X, ddof=1)
        diff1.append((E1 - mu) ** 2)
        diff2.append((E2 - sigma2) ** 2)
    Means.append(np.mean(diff1))
    Vars.append(np.mean(diff2))

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
x_axis = np.arange(2, repeat_num, 0.01)
axes[0].plot(x_axis, sigma2 / x_axis, color='green')
axes[0].scatter(range(2, i), Means)
axes[0].legend(["Теоретическая MSE выборочного среднего", "Вычисленная MSE выборочного среднего"])
axes[1].plot(x_axis, 2 * sigma2 ** 2 / (x_axis - 1), color='green')
axes[1].scatter(range(2, i), Vars)
axes[1].legend(["Теоретическая MSE несмещённой оценки дисперсии", "Вычисленная MSE несмещённой оценки дисперсии"])
axes[0].set(xlabel="Размер выборки", ylabel="MSE")
axes[1].set(xlabel="Размер выборки", ylabel="MSE")
plt.show()
fig.tight_layout()
plt.show()
