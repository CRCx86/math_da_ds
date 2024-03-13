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

alpha = 0.05
bootstrap_medians = sorted(bootstrap_medians)
left = int(alpha / 2 * k)
right = int((1 - alpha / 2) * k)
x1 = bootstrap_medians[left]
x2 = bootstrap_medians[right]
plt.hlines(y=0.005, xmin=x1, xmax=x2, linewidth=2, color='r')
plt.hist(bootstrap_medians, density=True, bins=10)
plt.show()
