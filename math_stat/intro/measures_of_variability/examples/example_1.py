import numpy as np

# Сгенерируем для примера выборку.
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Посчитаем среднее.
avg_value = np.mean(x)
print(avg_value)  # -> 4.5

# Посчитаем дисперсию.
var_value = np.var(x, ddof=1)
print(var_value)  # -> 6.0
