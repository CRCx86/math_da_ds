import scipy.stats as st
import numpy as np


def sampleS_n(Xi, n, K):  # Функция для создания набора значений величины Sn
    X = []  # Массив для хранения случайных величин X_i
    for i in range(n):  # Добавление n раз новой случайной величины X_i в массив X
        X.append(Xi)  # Добавление новой случайной величины X_i в массив X

    Sn = []  # Массив для хранения значений величины S_n
    for j in range(K):  # Повторяем K раз для получения K значений величины S_n
        S_j = 0  # Очередное значение, которое приняла величина S_n
        values = []  # Массив, в котором хранятся значения, которые приняли величины X_i
        for i in range(n):  # Проходим по каждой случайной величине из нашего набора
            X_i_value = X[i].rvs(size=1).item()  # Записываем в переменную значение,
            # которое приняла случайная величина X_i
            values.append(X_i_value)  # Добавляем значение,
            # которое приняла случайная величина X_i в наш массив
        S_j = sum(values)  # Получаем значение, принятое случайной величиной S_n
        Sn.append(S_j)  # Добавляем новое значение, принятое случайной величиной S_n, в массив
    return Sn


n1 = 5  # Число случайных величин X_i для первого графика
n2 = 50  # Число случайных величин X_i для второго графика
a = 0  # Параметр a равномерного распределения
b = 10  # Параметр b равномерного распределения
mu = (a + b) / 2  # Математическое ожидание величин X_i
sigma2 = (b - a) * (b - a) / 12  # Дисперсия величин X_i
K = 10000  # Количество получаемых значений величины S_n
Xi = st.uniform(a, b)

S1 = sampleS_n(Xi, n1, K)  # Набор значений величины S_n при n = 5
S2 = sampleS_n(Xi, n2, K)  # Набор значений величины S_n при n = 50

plot(S1, S2, n1, n2, mu, sigma2)
