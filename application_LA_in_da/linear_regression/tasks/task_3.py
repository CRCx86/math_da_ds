import numpy as np

X = np.array(
    [
        [2, 1, 1],
        [2, -4, 1],
        [0, -3, 1],
        [1, -4, 1],
        [-2, -5, 1],
        [-3, -1, 1]
    ]
)

y = np.array(
    [
        0.79360363,
        4.12033812,
        5.08632068,
        8.02628284,
        8.93128108,
        9.73436965
    ]
)

x_test = [1, -2, 1]

w = np.linalg.inv(X.T @ X) @ X.T @ y

result = x_test @ w

print(w)
print(result)
