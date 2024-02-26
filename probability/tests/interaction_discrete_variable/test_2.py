import pandas as pd
# Импортируйте необходимые библиотеки.
from scipy import stats

df = pd.read_csv("https://code.s3.yandex.net/Math/datasets/titanic.csv")

# Здесь ваш код.
age = df['Age']

result = stats.mode(age)

print(result)
