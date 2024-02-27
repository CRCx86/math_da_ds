import numpy as np

x1 = [8.91, 2.46, 2.60, 6.31, 12.2, 2.48, 3.68, 5.11,
      0.21, 7.13, 12.8, 6.90, 8.15, 0.70, 0.95, 3.38,
      -0.5, 10.7, 3.59, 5.73]  # Старый набор значений, собранных Максом и Ульяной

x2 = [3.14, 2.30, 4.10, 2.56, 7.65, 4.75, 2.38, 1.18,
      5.86, 8.11, 9.68, 1.14, 1.21, 1.71, 6.15, 8.50,
      6.20, 7.16, 9.85, 1.57]  # Новый набор значений, собранных Максом и Ульяной

avr_value_1 = np.mean(x1)
avr_value_2 = np.mean(x2)
print("Среднее")
print(f"Старое: {avr_value_1}")
print(f"Новое : {avr_value_2}\n")

var_value_1 = np.var(x1)
var_value_2 = np.var(x2)
print("Дисперсия")
print(f"Старая: {var_value_1}")
print(f"Новая : {var_value_2}\n")

std_value_1 = np.std(x1)
std_value_2 = np.std(x2)
print("Стандартное отклонение")
print(f"Старое: {std_value_1}")
print(f"Новое : {std_value_2}\n")

min_max_1 = np.max(x1) - np.min(x1)
min_max_2 = np.max(x2) - np.min(x2)
print("Расстояние между максимумом и минимумом")
print(f"Старое: {min_max_1}")
print(f"Новое : {min_max_2}\n")
