import numpy as np
import matplotlib.pyplot as plt

# Часы после начала смены.
hours = np.array([0., 1., 2., 3., 4., 5., 6., 7., 8., 0., 1., 2., 3., 4., 5., 6., 7.,
                  8., 0., 1., 2., 3., 4., 5., 6., 7., 8., 0., 1., 2., 3., 4., 5., 6.,
                  7., 8., 0., 1., 2., 3., 4., 5., 6., 7., 8., 0., 1., 2., 3., 4.])

# Оценка настроения.
mood = np.array([9., 7.5, 7.5, 10., 5.5, 7.5, 8.5, 5., 5.5, 5., 7.,
                 8.5, 8.5, 5., 6.5, 8.5, 3.5, 3., 5.5, 6., 7., 7.,
                 5.5, 6., 8.5, 7., 6., 6., 8., 10., 7., 6., 4.5,
                 6.5, 4.5, 6.5, 7., 8.5, 6., 6.5, 9.5, 8., 8., 5.,
                 3.5, 6., 9., 6.5, 5.5, 8.])

# Напишите ваш код здесь.
ones = np.ones(len(mood))

X = np.stack([hours, ones], axis=1)

w = np.linalg.inv(X.T @ X) @ X.T @ mood

print(w)

# Код для построения графика, можно не менять.
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], mood, s=100)

x_min, x_max = hours.min() - 1, hours.max() + 1
plt.xlim(x_min, x_max)

y_min, y_max = 0, 11
plt.ylim(y_min, y_max)

y_min_line = x_min * w[0] + w[1]
y_max_line = x_max * w[0] + w[1]

plt.plot(
    [x_min, x_max],
    [y_min_line, y_max_line],
    linewidth=3,
    c="C1",
)

plt.xlabel("$x$", fontsize=15)
plt.ylabel("$y$", fontsize=15, rotation=0, labelpad=15)

plt.grid()
plt.show()
