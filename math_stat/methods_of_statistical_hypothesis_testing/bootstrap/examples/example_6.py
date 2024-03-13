import numpy as np
import pandas as pd

times = pd.read_csv('https://code.s3.yandex.net/Math/datasets/Times.csv', header=None).values.flatten().tolist()

n = len(times)
k = 1500

bootstrap_medians = []
i = 0

while i < k:
    bootstrap_values = np.random.choice(times, n, True)
    med = np.median(bootstrap_values)
    bootstrap_medians.append(med)
    i += 1

med_mean = np.mean(bootstrap_medians)
med_std = np.std(bootstrap_medians, ddof=1)

print("Оценка медианы из исходного набора данных:", np.median(times))
print("Среднее значение медианы по всем поднаборам данных:", med_mean)
print("Оценка стандартного отклонения медианы:", med_std)
