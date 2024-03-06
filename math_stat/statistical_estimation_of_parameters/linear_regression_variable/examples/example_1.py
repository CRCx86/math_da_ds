import numpy as np
import scipy.stats

X = sorted([52, 37, 53, 74, 52, 55, 41])
Y = [i for i in range(140, 210, 10)]
linregress = scipy.stats.linregress(X, Y)
print(linregress)

R = linregress[2] ** 2

print("Полученное значение R^2 =", R)
