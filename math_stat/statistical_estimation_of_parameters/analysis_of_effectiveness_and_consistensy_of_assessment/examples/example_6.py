import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

mu = 5
sigma2 = 10
i = 0
repeat_num = 50
step = 4
data = []

while i < repeat_num:
    ar = []
    i = i + step
    for j in range(100):
        X = np.random.normal(mu, np.sqrt(sigma2), i)
        E1 = np.mean(X)
        ar.append(E1)
    if i % step == 0:
        data.append(ar)

plt.figure(figsize=(12, 6))
densities = list(map(gaussian_kde, data))
xs = np.linspace(np.mean(data[0]) - 4 * np.std(data[0]),
                 np.mean(data[0]) + 4 * np.std(data[0]), 200)
i = 0
while i < len(densities):
    plt.plot(xs, densities[i](xs))
    i += 1

plt.xlabel('x')
plt.ylabel('Вероятность')
plt.legend(title='Число элементов в выборке', loc='upper left',
           labels=list(map(str, range(1, repeat_num, step))))
plt.show()
