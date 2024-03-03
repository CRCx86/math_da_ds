import numpy as np
import pandas as pd

# Загрузим датасет titanic.csv из прошлого урока.
df = pd.read_csv("https://code.s3.yandex.net/Math/datasets/titanic.csv")

# 1) способ 1 (NumPy)
avg_1 = np.mean(df["Fare"].to_numpy())
print(avg_1)  # -> 32.204207968574636

# 1) способ 2 (pandas)
avg_2 = df["Fare"].mean()
print(avg_2)  # -> 32.204207968574636
