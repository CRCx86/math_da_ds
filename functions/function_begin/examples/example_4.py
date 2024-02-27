import numpy as np
from matplotlib import pyplot as plt

data = np.array([
    [54.5, 5, 29.659],
    [85.4, 20, 44.632],
    [34.3, 5, 10.908],
    [43, 18, 20]
])

# Точки квартир.
area = data[:, 0]
price = data[:, 2]

# plt.scatter(area, price)
plt.plot(area, price)

# Точки прямой.
# Диапазон (30, 90) взят на глаз, попробуйте его изменить.
x = np.arange(30, 90, 1)
y = 0.5 * x

# plt.plot(x, y)
plt.scatter(x, y)
