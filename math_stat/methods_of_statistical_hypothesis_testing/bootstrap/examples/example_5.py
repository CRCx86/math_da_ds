import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

times = pd.read_csv('https://code.s3.yandex.net/Math/datasets/Times.csv', header=None).values.flatten().tolist()

n = len(times)
k = 1500

newarr = []

i = 0
while i < k:
    bootstrap_values = np.random.choice(times, n, True)
    newarr = np.concatenate((newarr, bootstrap_values))
    i += 1

print(len(newarr))

plt.figure()
plt.subplot(121)
plt.hist(newarr, density=True, bins=20)

plt.subplot(122)
plt.hist(times, density=True, bins=20)
plt.show()
