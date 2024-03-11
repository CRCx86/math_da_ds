from scipy import stats

# Определим случайную величину с помощь распределения Стьюдента.
# С помощью параметра df передадим количество степеней свободы (m).
T = stats.t(df=10)

# Вычислим значение t_10,0.01.
t_001 = T.ppf(q=1 - 0.01)

# Выведем полученное значение.
print(t_001)
