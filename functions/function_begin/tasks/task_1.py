import numpy as np
import pandas as pd

# Считывание данных из файла drive-data.csv.
# В cars_data лежит двумерный NumPy-массив (таблица) из условия.
cars_data = pd.read_csv('drive-data.csv').values

print(cars_data[:, 0])
print(cars_data[len(cars_data) - 1, :])
print(cars_data[0, 3])