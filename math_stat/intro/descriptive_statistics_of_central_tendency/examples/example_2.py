import numpy as np

# Сгенерируем для примера случайную выборку из Binomial(n=1000, p=0.5).
x = np.random.binomial(1000, 0.5, 10000)

avg_value = np.mean(x)
print(avg_value)  # -> Получится значение в районе 500.
