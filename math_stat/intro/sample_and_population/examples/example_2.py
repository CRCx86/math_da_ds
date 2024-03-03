import numpy as np
from matplotlib import pyplot as plt

x_10 = np.random.binomial(1, 0.5, 10)
x_100 = np.random.binomial(1, 0.5, 100)
x_1000 = np.random.binomial(1, 0.5, 1000)

val_10, cnt_10 = np.unique(x_10, return_counts=True)
pmf_10 = cnt_10 / len(x_10)

val_100, cnt_100 = np.unique(x_100, return_counts=True)
pmf_100 = cnt_100 / len(x_100)

val_1000, cnt_1000 = np.unique(x_1000, return_counts=True)
pmf_1000 = cnt_1000 / len(x_1000)

# Для выборки из 10 значений выведем, что мы получили.
print(val_10)  # -> [0 1] — уникальные значения
print(cnt_10)  # -> [6 4] — количество
print(pmf_10)  # -> [0.6 0.4] — относительная частота

plt.bar(val_10, pmf_10)
plt.show()

# Для выборки из 100 значений выведем, что мы получили.
print(val_100)
print(cnt_100)
print(pmf_100)

plt.bar(val_100, pmf_100)
plt.show()

# Для выборки из 1000 значений выведем, что мы получили.
print(val_1000)
print(cnt_1000)
print(pmf_1000)

plt.bar(val_1000, pmf_1000)
plt.show()
