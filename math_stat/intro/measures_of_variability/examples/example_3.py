import numpy as np

# Сгенерируем выборку для примера.
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Размах.
range_value = np.max(x) - np.min(x)
print(range_value)  # -> 7
