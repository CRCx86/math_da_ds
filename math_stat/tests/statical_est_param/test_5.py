import numpy as np

a = 1
b = 7
repeat_num = 10
theta = []
i = 0

while i < repeat_num:
    X = np.random.uniform(a, b, 10)
    theta.append(np.var(X, ddof=1))
    i += 1

MSE = 0  # Переменная для вычисления MSE

# Ваш код здесь
t_var = (b - a) ** 2 / 12
MSE = np.mean((np.array(theta) - t_var) ** 2)

print("MSE данного набора оценок равно:", MSE)
