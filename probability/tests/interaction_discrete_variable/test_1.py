import pandas as pd
import numpy as np

df = pd.read_csv("https://code.s3.yandex.net/Math/datasets/titanic.csv")

survived = df['Survived']

# Здесь ваш код.
result = np.mean(survived)

print(result)
