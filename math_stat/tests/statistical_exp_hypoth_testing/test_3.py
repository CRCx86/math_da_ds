import numpy as np

# Допишите код здесь.
from scipy import stats

x = np.array([642, 591, 591, 618, 624, 603, 591, 609, 627])

# Допишите код здесь.
n = len(x)
sigma = np.std(x, ddof=1)

t_stat = (np.mean(x) - 600) / (sigma / np.sqrt(n))

T = stats.t(df=8)
t_crit = T.ppf(q=1 - 0.025)

print("Статистика критерия равна", t_stat)
print("Критическое значение равно", t_crit)

if abs(t_stat) > t_crit:
    print("Отклоняем нулевую гипотезу на уровне значимости 5%")
else:
    print("Не отклоняем нулевую гипотезу на уровне значимости 5%")
