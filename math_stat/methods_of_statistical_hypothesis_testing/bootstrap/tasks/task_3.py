import numpy as np
import pandas as pd

n = 400

X = pd.read_csv('https://code.s3.yandex.net/Math/datasets/Z.csv', header=None).values.flatten().tolist()

k = 1000  # число выборок бутстрепа
f = len(X)  # размер выборки бутстрепа

left = 0
right = 0
# Ваш код

bootstrap_vars = []
i = 0
while i < k:
    bs_val = np.random.choice(X, f, True)
    var = np.var(bs_val)
    bootstrap_vars.append(var)
    i += 1

alpha = 0.1
bootstrap_vars = sorted(bootstrap_vars)

i = int(alpha / 2 * k)
j = int((1 - alpha / 2) * k)

left = bootstrap_vars[i]
right = bootstrap_vars[j]

print(left)
print(right)
