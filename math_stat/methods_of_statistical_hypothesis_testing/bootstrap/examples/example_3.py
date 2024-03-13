import numpy as np
import pandas as pd

times = pd.read_csv('https://code.s3.yandex.net/Math/datasets/Times.csv', header=None).values.flatten().tolist()

n = len(times)
k = 200
meds = []
i = 0

while i < k:
    time = times[i * (n // k): (i + 1) * (n // k)]
    med = np.median(time)
    meds.append(med)
    i += 1

med_mean = np.mean(meds)
med_std = np.std(meds, ddof = 1)

print("Оценка медианы из исходного набора данных:", np.median(times))
print("Среднее значение медианы по всем поднаборам данных:", med_mean)
print("Оценка стандартного отклонения медианы:", med_std)