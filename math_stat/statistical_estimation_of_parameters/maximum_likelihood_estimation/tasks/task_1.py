import numpy as np
from scipy.stats import expon

Lambda = 1 / 1.5
size = 1000
X = np.random.exponential(Lambda, size)  # это обычно неизвестно
theta1 = 10
theta2 = 2
diff = 0

# Вставьте ваш код вычисления разности функций правдоподобия
diff = expon.pdf(x=np.mean(X), scale=1/theta1) - expon.pdf(x=np.mean(X), scale=1/theta2)

if diff < 0:
    print("Оценка theta = 2 точнее.")
else:
    print("Оценка theta = 10 точнее.")
