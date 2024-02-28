import matplotlib.pyplot as plt

X_vals = [2.64, 8.50, 5.40, 2.54, 3.98, 3.49, 8.68, 1.08,
          3.40, 1.81, 9.41, 4.92, 5.865, 1.31, 12.15, 4.50,
          2.20, 1.16, 8.85, 8.57]
plt.hist(X_vals, density=True, bins=8)
plt.show()
