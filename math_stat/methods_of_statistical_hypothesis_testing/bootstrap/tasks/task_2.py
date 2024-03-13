import numpy as np
import pandas as pd

X = pd.read_csv('https://code.s3.yandex.net/Math/datasets/Z.csv', header=None).values.flatten().tolist()

n = len(X)
k = 1000  # число выборок бутстрепа
f = len(X)  # размер выборки бутстрепа

# Ваш код
stds = []
i = 0
while i < k:
    bs = np.random.choice(X, f, True)
    std = np.std(bs, ddof=1)
    stds.append(std)
    i += 1

result = np.std(stds, ddof=1)
print(result)
