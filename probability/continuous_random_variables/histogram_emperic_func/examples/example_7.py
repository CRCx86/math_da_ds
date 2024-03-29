import matplotlib.pyplot as plt

X_vals = [2.64, 8.50, 5.40, 2.54, 3.98, 3.49, 8.68, 1.08,
          3.40, 1.81, 9.41, 4.92, 5.865, 1.31, 12.15, 4.50,
          2.20, 1.16, 8.85, 8.57]

# Подготовим место для двух графиков
fig, axes = plt.subplots(1, 2)

# Вызовем функцию гистограммы от массива X_vals с параметром bins
axes[0].hist(X_vals, bins=5)
# Добавление названия к графику
axes[0].set_title("С параметром bins=5")

# Вызовем функцию гистограммы от массива X_vals без параметра bins
axes[1].hist(X_vals)
# Добавление названия к графику
axes[1].set_title("Без параметра bins")

# Вывод обоих графиков
plt.show()
