from scipy import stats

# С помощью параметра loc передадим математическое ожидание,
# а scale — стандартное отклонение.
Z = stats.norm(loc=0, scale=1)

z_001 = Z.ppf(q=1-0.01)
z_095 = Z.ppf(q=1-0.95)

print(z_001)
print(z_095)
