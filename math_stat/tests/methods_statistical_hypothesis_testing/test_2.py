import numpy as np
import pandas as pd

n = 1000

X = pd.read_csv('https://code.s3.yandex.net/Math/datasets/Problem_2.csv', header=None).values.flatten().tolist()

k = 1500  # Число выборок бутсрепа.
f = len(X)  # Размер выборки бутстрепа.

bootstrap_var = 0
bootstrap_stds = []

# Ваш код здесь.
i = 0
while i < k:
    choice = np.random.choice(X, f, True)
    bootstrap_stds.append(np.std(choice, ddof=1))
    i += 1

bootstrap_var = np.var(bootstrap_stds, ddof=1)

print("Дисперсия стандартного отклонения равна", bootstrap_var)
