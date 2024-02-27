import numpy as np
from matplotlib import pyplot as plt

data = np.array([
    [54.5, 5, 29.659],
    [85.4, 20, 44.632],
    [34.3, 5, 10.908],
    [43, 18, 20],
    [100, 3, 50],
])

area = data[:, 0]
price = data[:, 2]

plt.scatter(area, price)
