import pandas as pd

# Считывание данных из файла clients.csv.
df = pd.read_csv("https://code.s3.yandex.net/Math/datasets/clients.csv")

# Сохраним значения в колонках в уже привычном формате numpy array.
age = df["age"].to_numpy()
fav_platform = df["fav_platform"].to_numpy()

print(age)
print(fav_platform)
