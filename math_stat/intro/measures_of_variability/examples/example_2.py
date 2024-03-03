import numpy as np

# Сгенерируем для примера выборку.
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Среднее значение.
avg_value = np.mean(x)
print(avg_value)  # -> 4.5

# Дисперсия.
var_value = np.var(x, ddof=1)
print(var_value)  # -> 6.0

# Стандартное отклонение как корень из дисперсии.
std_value_1 = np.sqrt(np.var(x, ddof=1))
print(std_value_1)  # -> 2.449489742783178

# Стандартное отклонение с помощью специальной функции.
std_value_2 = np.std(x, ddof=1)
print(std_value_2)  # -> 2.449489742783178
