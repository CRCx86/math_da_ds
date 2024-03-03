import pandas as pd
# Дополнительно импортируйте необходимые библиотеки.
import numpy as np
from scipy import stats

# Преобразуем необходимые переменные в numpy array.
df = pd.read_csv("https://code.s3.yandex.net/Math/datasets/auto-mpg.csv")
kpl = df["kpl"].to_numpy()
cylinders = df["cylinders"].to_numpy()
years = df["model-year"].to_numpy()

# Здесь ваш код.
avg_kpl = np.mean(kpl)
med_kpl = np.median(kpl)
top_cylinders = stats.mode(cylinders).mode
top_year = stats.mode(years).mode

print(avg_kpl)
print(med_kpl)
print(top_cylinders)
print(top_year)
