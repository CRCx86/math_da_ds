import numpy as np

l = 1/np.sqrt(2)
n_size = 100

Y = np.random.exponential(l, n_size)

E_estim_unbiased = 0 # Переменная для оценки математического ожидания
Var_estim_unbiased = 0 # Переменная для оценки дисперсии

# Ваш код здесь
E_estim_unbiased = np.mean(Y)
Var_estim_unbiased = np.var(Y, ddof=1)

print("Несмещённая оценка математического ожидания:", E_estim_unbiased)
print("Несмещённая оценка дисперсии:", Var_estim_unbiased)