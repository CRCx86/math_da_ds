# Здесь ваш код.
from scipy import stats

T = stats.t(df=3)

t_001 = T.ppf(q=1 - 0.01)
t_099 = T.ppf(q=1 - 0.99)

print(t_001)
print(t_099)
