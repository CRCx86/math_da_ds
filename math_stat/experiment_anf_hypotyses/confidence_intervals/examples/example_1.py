from scipy import stats

# С помощью параметра loc передадим математическое ожидание,
# а scale — стандартное отклонение.
Z = stats.norm(loc=0, scale=1)

# Вычислим значение z_0.2.
z_02 = Z.ppf(q=1-0.2)

# Выведем полученное значение.
print(z_02)
