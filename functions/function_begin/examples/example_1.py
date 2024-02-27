import numpy as np

data = np.array([
    [54.5, 5, 29.659],
    [85.4, 20, 44.632],
    [34.3, 5, 10.908],
    [43, 18, 20]
])

print(data[1, 0])
print(data[2, 1])
print(data[0, 0])
print(data[len(data) - 1, len(data[0]) - 1])
