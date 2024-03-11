import numpy as np

# Допишите код здесь.
from scipy import stats

x = np.array([14, 15, 15, 16, 13, 8, 14,
              17, 16, 14, 19, 20, 21, 15,
              15, 16, 16, 13, 14, 12])

y = np.array([15, 17, 14, 17, 14, 8, 12,
              19, 19, 14, 17, 22, 24, 16,
              13, 16, 13, 18, 15, 13])

# Допишите код здесь.
n_x = len(x)
n_y = len(y)

std_x = np.std(x, ddof=1)
std_y = np.std(y, ddof=1)

mean_x = np.mean(x)
mean_y = np.mean(y)

s = np.sqrt(((n_x - 1) * (std_x ** 2) + (n_y - 1) * (std_y ** 2)) / (n_x + n_y - 2))
t_stat = (mean_x - mean_y) / np.sqrt((s ** 2 / n_x) + (s ** 2 / n_y))

T = stats.t(df=n_x+n_y-2)
t_crit = T.ppf(q=1 - 0.005)

print("Статистика критерия равна", t_stat)
print("Критическое значение равно", t_crit)

if abs(t_stat) > t_crit:
    print("Отклоняем нулевую гипотезу на уровне значимости 1%")
else:
    print("Не отклоняем нулевую гипотезу на уровне значимости 1%")
