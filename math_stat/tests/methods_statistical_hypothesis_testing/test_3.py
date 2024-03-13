import numpy as np
import pandas as pd

n = 1000

X = pd.read_csv('https://code.s3.yandex.net/Math/datasets/Problem_2.csv', header=None).values.flatten().tolist()

k = 1500  # Число выборок бутсрепа.
f = len(X)  # Размер выборки бутстрепа.

left = 0
right = 0

bootstrap_stds = []

# Ваш код здесь.
i = 0
while i < k:
    choice = np.random.choice(X, f, True)
    bootstrap_stds.append(np.std(choice, ddof=1))
    i += 1

alpha = 0.1
bootstrap_stds = sorted(bootstrap_stds)

i = int(alpha / 2 * k)
j = int((1 - alpha / 2) * k)

left = bootstrap_stds[i]
right = bootstrap_stds[j]

print("Самый левый элемент выборки из доверительного интервала:", left)
print("Самый правый элемент выборки из доверительного интервала:", right)
