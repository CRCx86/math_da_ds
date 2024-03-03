import numpy as np
from scipy import stats

# Сгенерируем выборку для примера.
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Размах.
iqr_value = stats.iqr(x)
print(iqr_value)  # -> 3.5
