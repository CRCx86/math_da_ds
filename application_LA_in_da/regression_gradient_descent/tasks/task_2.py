import numpy as np
import matplotlib.pyplot as plt

x = np.array([-0.52167305, 0.27831481, 0.14501393, 1.63219094, -0.61142463,
              -0.10026818, -0.56852301, 0.92413066, -1.06796546, -0.23646856,
              1.16774726, -1.32774771, -1.16892254, 0.54870376, 2.56270657,
              1.4272611, 0.70309839, 0.66520861, 0.6381659, -1.55504931])
y = np.array([-36.19864852, 27.0996779, 4.13602061, 23.56341085,
              -15.51140579, -9.56641513, -19.52974424, 39.2287813,
              -42.75598725, 7.21673981, 1.22945187, -58.73526603,
              -1.25511398, 11.36308065, 57.6580178, 49.45754646,
              35.13876746, 10.56182559, 18.76715253, -71.95313197])

# Напишите ваш код здесь.
X = np.stack([x, np.ones(len(x))], axis=1)
w = np.linalg.inv(X.T @ X) @ X.T @ y

print(w)

# Код для построения графика, его можно не менять.
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], y, s=100)

x_min, x_max = x.min() - 1, x.max() + 1
plt.xlim(x_min, x_max)

y_min, y_max = y.min() - 1, y.max() + 1
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
# plt.show()
