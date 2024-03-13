from scipy import stats
import numpy as np
import pandas as pd

times = pd.read_csv('https://code.s3.yandex.net/Math/datasets/Times.csv', header=None).values.flatten().tolist()

n = len(times)
k = 1500

Z = stats.norm(loc=0, scale=1)
alpha = 0.05
z = Z.ppf(q=1 - alpha / 2)

bootstrap_medians = []
i = 0
while i < k:
    bootstrap_values = np.random.choice(times, n, True)
    bootstrap_medians.append(np.median(bootstrap_values))
    i += 1

me_mean = np.mean(bootstrap_medians)
me_std = np.std(bootstrap_medians)
me_left = me_mean - z * me_std / np.sqrt(k)
me_right = me_mean + z * me_std / np.sqrt(k)

print(me_mean)
print("Медиана с вероятностью 95% лежит в диапазоне: (", me_left, ",", me_right, ")")
