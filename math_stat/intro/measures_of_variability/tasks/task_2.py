import numpy as np
from scipy import stats

x = np.array([1, 2, 4, 3, 1, 5, 4, 3, 3, 1, 2, 4, 2, 3, 2, 4, 2, 2, 5, 4])

# Здесь ваш код.
var_value = np.var(x, ddof=1)
std_value = np.std(x, ddof=1)
range_value = np.max(x) - np.min(x)
iqr_value = stats.iqr(x)

print(var_value)  # должно вывести дисперсию
print(std_value)  # должно вывести стандартное отклонение
print(range_value)  # должно вывести размах
print(iqr_value)  # должно вывести межквартильный размах
