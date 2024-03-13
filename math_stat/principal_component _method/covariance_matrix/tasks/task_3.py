# Допишите код здесь
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

price = [2550, 1920, 2200, 1950, 1987, 2030, 2655, 1855]
age = [1, 2, 1, 2, 2, 2, 0, 2]
km = [40, 39269, 36822, 32834, 35255, 59005, 10910, 20627]

labs = ['Цена', 'Возраст', 'Пробег']

print("Матрица ковариации:")
# Допишите код здесь
price = np.array(price)
age = np.array(age)
km = np.array(km)

cov = (price - price.mean()) @ (age - age.mean()) / (len(price) - 1)
cov_price_km = (price - price.mean()) @ (km - km.mean()) / (len(age) - 1)
cov_age_km = (age - age.mean()) @ (km - km.mean()) / (len(km) - 1)

cov_mat = np.array([
    [np.var(price, ddof=1), cov, cov_price_km],
    [cov, np.var(age, ddof=1), cov_age_km],
    [cov_price_km, cov_age_km, np.var(km, ddof=1)],
])
print(cov_mat)

sns.heatmap(
    cov_mat,  # не забудьте определить переменную
    annot=True,
    fmt='g',
    xticklabels=labs,
    yticklabels=labs
)
plt.show()
