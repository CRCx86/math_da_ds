from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

times = pd.read_csv('https://code.s3.yandex.net/Math/datasets/Times_Short.csv', header=None).values.flatten().tolist()

n = len(times)
k = 1500

bootstrap_medians = []
i = 0
while i < k:
    bootstrap_values = np.random.choice(times, n, True)
    bootstrap_medians.append(np.median(bootstrap_values))
    i += 1

plt.hist(bootstrap_medians, density=True)
plt.show()
