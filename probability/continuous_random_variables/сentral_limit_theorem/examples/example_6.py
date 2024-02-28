import scipy.stats as st
import numpy as np


def sampleMean_X_n(a, b, n, K):  # Функция для создания набора значений величины Sn
    X = []  # Массив для хранения случайных величин X_i
    for i in range(n):  # Добавление n раз новой случайной величины X_i в массив X
        X.append(st.uniform(a, b))  # Добавление новой случайной величины X_i в массив X

    Mean_X_n = []  # Массив для хранения значений величины \bar{X}_n
    for j in range(K):  # Повторяем K раз для получения K значений величины \bar{X}_n
        S_j = 0  # Очередное значение, которое приняла величина \bar{X}_n
        values = []  # Массив, в котором хранятся значения, которые приняли величины X_i
        for i in range(n):  # Проходим по каждой случайной величине из нашего набора
            X_i_value = X[i].rvs(size=1).item()  # Записываем в переменную значение,
            # которое приняла случайная величина X_i
            values.append(X_i_value)  # Добавляем значение,
            # которое приняла случайная величина X_i в наш массив
        Mean_X_j = np.mean(values)  # Получаем значение, принятое случайной величиной \bar{X}_n
        Mean_X_n.append(Mean_X_j)  # Добавляем новое значение, принятое случайной величиной \bar{X}_n, в массив
    return Mean_X_n


n1 = 5  # Число случайных величин X_i для первого графика
n2 = 50  # Число случайных величин X_i для второго графика
a = 0  # Параметр a равномерного распределения
b = 10  # Параметр b равномерного распределения
mu = (a + b) / 2  # Математическое ожидание величин X_i
sigma2 = (b - a) * (b - a) / 12  # Дисперсия величин X_i
K = 10000  # Количество получаемых значений величины \bar{X}_n

Mean_X1 = sampleMean_X_n(a, b, n1, K)  # Набор значений величины \bar{X}_n при n = 5
Mean_X2 = sampleMean_X_n(a, b, n2, K)  # Набор значений величины \bar{X}_n при n = 50

plot(Mean_X1, Mean_X2, n1, n2, mu, sigma2)
