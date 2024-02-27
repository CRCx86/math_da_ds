# Подключение необходимой библиотеки
from scipy import stats

# Параметры равномерного распределения
a = 1
b = 12

# Размер выборки
n_size = 10

# Создание случайной величины необходимого типа
X = stats.uniform(loc=a, scale=b - a)

# Создание выборки случайной величины
Sample_X = X.rvs(n_size)

print(Sample_X)
