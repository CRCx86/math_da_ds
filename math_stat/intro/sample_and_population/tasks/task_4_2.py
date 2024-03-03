import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("https://code.s3.yandex.net/Math/datasets/titanic.csv")
pclass = df["Pclass"].to_numpy()
age = df["Age"].to_numpy()

# Здесь ваш код.
bins = np.arange(0, 100, 1)

plt.hist(age, bins=bins, weights=np.ones_like(age) / len(age))
plt.show()
