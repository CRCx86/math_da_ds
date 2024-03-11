# Здесь ваш код.
from scipy import stats

Z = stats.norm(loc=0, scale=1)

z_005 = Z.ppf(q=0.005)
z_025 = Z.ppf(q=0.025)

print(z_005)
print(z_025)
