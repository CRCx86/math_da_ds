import pandas as pd
# Импортируйте необходимые библиотеки.
import numpy as np
from scipy import stats

df = pd.read_csv("https://code.s3.yandex.net/Math/datasets/titanic.csv")
fare = df["Fare"].to_numpy()

# Здесь ваш код.
range_value = np.max(fare) - np.min(fare)
iqr_value = stats.iqr(fare)

print(range_value)
print(iqr_value)
