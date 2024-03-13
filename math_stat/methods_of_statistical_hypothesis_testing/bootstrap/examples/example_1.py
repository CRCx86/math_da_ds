import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

times = pd.read_csv('https://code.s3.yandex.net/Math/datasets/Times.csv', header=None).values.flatten().tolist()
mean = np.mean(times)
std = np.std(times)
print("Оценка среднего значения времени ожидания:", mean)
print("Оценка стандартного отклонения времени ожидания:", std)

plt.hist(times, density=True)
plt.show()

med = np.median(times)
print("Медиана полученного набора данных равна", med, "секунд")
