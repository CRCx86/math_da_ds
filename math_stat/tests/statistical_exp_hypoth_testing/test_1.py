# Здесь ваш код.
from scipy import stats

t_100 = stats.t(df=100).ppf(1 - 0.01)
t_50 = stats.t(df=50).ppf(1 - 0.01)

print(t_100) # Случайная величина ~ t(100)
print(t_50) # Случайная величина ~ t(50)