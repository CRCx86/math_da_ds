import scipy.stats as st

max_digits = 5  # Количество выводимых цифр
n = 5  # Число случайных величин X_i
a = 0  # Параметр a равномерного распределения
b = 10  # Параметр b равномерного распределения

X = []  # Массив для хранения случайных величин X_i
for i in range(n):  # Добавление n раз новой случайной величины X_i в массив X
    X.append(st.uniform(a, b))  # Добавление новой случайной величины X_i в массив X

values = []  # Массив, в котором хранятся значения, которые приняли величины X_i
for i in range(n):  # Проходим по каждой случайной величине из нашего набора
    X_i_value = X[i].rvs(size=1).item()  # Записываем в переменную значение,
    # которое приняла случайная величина X_i
    values.append(X_i_value)  # Добавляем значение,
    # которое приняла случайная величина X_i в наш массив

for i in range(n):  # Проходим по каждой случайной величине из нашего набора
    print("Случайная величина X_", i + 1, " приняла значение: ", str(values[i])[:max_digits], sep="")
    # Вывод значения, которое приняла каждая случайная величина X_i

print("Тогда случайная величина S_n приняла значение:", str(sum(values))[:max_digits])
# Вывод значения, которое приняла случайная величина S_n
