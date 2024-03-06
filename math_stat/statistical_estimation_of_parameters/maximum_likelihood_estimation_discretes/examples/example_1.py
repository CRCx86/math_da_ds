import scipy as sp
import scipy.special
import numpy as np
import matplotlib.pyplot as plt


# Функция определяет наиболее вероятный p при фиксированном m
def p_estimator(m, Y):
    return np.mean(Y) / m


# Определим логарифм функции правдоподобия
def LogL(m, p, Y):
    result = 0

    i = 0
    n = len(Y)
    while (i < n):
        # Логарифмы биномиальных коэффициентов
        result = result + np.log(float(sp.special.binom(m, Y[i])))
        i = i + 1

    # И два оставшихся слагаемых
    result = result + np.log(p) * np.sum(Y)
    result = result + np.log(1 - p) * (m * n - np.sum(Y))

    return result


# Теперь создаём функцию g:
def g(m, Y):
    return LogL(m, p_estimator(m, Y), Y)


# Задаём тестовую случайную величину с известными параметрами распределения
m_param = 24
p_param = 0.2
sz = 1000
X = np.random.binomial(m_param, p_param, size=sz)

# Устанавливаем параметр N — длину отрезка
start_m = np.max(X)
N_length = 50
finish_m = start_m + N_length

# Ищем максимальный элемент
m_vals = []
g_vals = []

m = start_m
while (m <= finish_m):
    m_vals.append(m)
    g_vals.append(g(m, X))
    m = m + 1

# Значение наибольшего элемента
ind_max = g_vals.index(np.max(g_vals))
m_max = start_m + ind_max

# Находим соответствующий p
p_est = p_estimator(m_max, X)

# Возвращаем результаты
print("Настоящие значения параметров:")
print(f"p = {p_param}, m = {m_param};")
print("Оценки по ММП:")
print(f"p = {p_est}, m = {m_max}.")

# Иллюстрация с помощью графика
plt.scatter(m_vals, g_vals)
plt.xlabel("Параметр m")
plt.ylabel("Функция g(m)")
plt.show()
