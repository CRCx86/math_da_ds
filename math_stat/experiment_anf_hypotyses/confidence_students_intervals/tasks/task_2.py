# Здесь ваш код.
from scipy import stats

T = stats.t(df=15)
t_005 = T.ppf(q=1 - 0.005)

T = stats.t(df=50)
t_025 = T.ppf(q=1 - 0.025)

print(t_005)
print(t_025)
