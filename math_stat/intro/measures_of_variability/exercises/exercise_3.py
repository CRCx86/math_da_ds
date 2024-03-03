import pandas as pd
import numpy as np
from scipy import stats

# Считывание данных из файла clients.csv.
df = pd.read_csv("https://code.s3.yandex.net/Math/datasets/clients.csv")
age = df["age"].to_numpy()
fav_platform = df["fav_platform"].to_numpy()

# Здесь ваш код.
result = np.max(age) - np.min(age)

print(result)
