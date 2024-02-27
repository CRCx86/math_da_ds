# Подключение необходимой библиотеки
from scipy import stats

# Параметр экспоненциального распределения
Lambda = 0.2

# Размер выборки
n_size = 10

# Создание случайной величины необходимого типа
X = stats.expon(scale=1 / Lambda)

# Создание выборки случайной величины
Sample_X = X.rvs(n_size)

print(Sample_X)
