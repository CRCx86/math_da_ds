import numpy as np
import scipy.stats

X = sorted(np.random.uniform(0, 20, 50))
Y = sorted(np.random.exponential(1 / 5, 50))
R = 0

# Ваш код
linregress = scipy.stats.linregress(X, Y)
R = linregress[2] ** 2

print("Полученное значение R^2 =", R)
