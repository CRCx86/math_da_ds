import numpy as np

l = 10
n_size = 100

Y = np.random.exponential(1 / l, n_size)
estim_biased = 0  # Смещенная дисперсия
estim_unbiased = 0  # Несмещенная дисперсия

# Ваш код здесь
estim_biased = np.var(Y)
estim_unbiased = np.var(Y, ddof=1)

print("Смещённая оценка дисперсии:", estim_biased)
print("Несмещённая оценка дисперсии:", estim_unbiased)
print("Истинное значение дисперсии:", 1 / (l * l))
