import numpy as np
import scipy.stats
from sklearn.linear_model import LinearRegression

Y = sorted(np.random.uniform(0, 20, 10))
X_1 = sorted(np.random.exponential(6, 10))
X_2 = sorted(np.random.normal(4, 2, 10))

R1 = 0
R2 = 0

# Ваш код
X_1 = np.array(X_1)
X_2 = np.array(X_2)
Y = np.array(Y)

model1 = LinearRegression()
model1.fit(X_1.reshape(-1, 1), Y.reshape(-1, 1))
R1 = scipy.stats.linregress(X_1, Y)[2] ** 2

model2 = LinearRegression()
model2.fit(X_2.reshape(-1, 1), Y.reshape(-1, 1))
R2 = scipy.stats.linregress(X_2, Y)[2] ** 2

if R1 > R2:
    print("Модель на основе X1 лучше по R^2")
else:
    print("Модель на основе X2 лучше по R^2")
