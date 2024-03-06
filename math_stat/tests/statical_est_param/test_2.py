import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Импортируйте необходимые библиотеки.

df = pd.read_csv("https://code.s3.yandex.net/Math/datasets/titanic.csv")
surv = df["Survived"].to_numpy()

# Здесь ваш код.
val, cnt = np.unique(surv, return_counts=True)
pmf = cnt / len(surv)

plt.bar(val, pmf)
plt.show()
