import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("https://code.s3.yandex.net/Math/datasets/titanic.csv")
pclass = df["Pclass"].to_numpy()
age = df["Age"].to_numpy()

# Здесь ваш код.
val, cnt = np.unique(pclass, return_counts=True)
pmf = cnt / len(pclass)

plt.bar(val, pmf)
plt.show()
