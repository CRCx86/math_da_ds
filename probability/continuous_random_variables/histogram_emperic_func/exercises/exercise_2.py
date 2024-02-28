from scipy import stats
import matplotlib.pyplot as plt

n_size = 1000

# Параметры равномерного распределения.
a = 3
b = 7

# Параметры экспоненциального распределения.
Lambda = 2

# Напишите ваш код здесь.
X = stats.uniform(loc=a, scale=b - a)
Sample_X = X.rvs(n_size)  # Выборка из 1000 значений для случайной величины X.
Y = stats.expon(scale=1 / Lambda)
Sample_Y = Y.rvs(n_size)  # Выборка из 1000 значений для случайной величины Y.

plt.hist(Sample_X)
plt.show()

plt.hist(Sample_Y)
plt.show()
