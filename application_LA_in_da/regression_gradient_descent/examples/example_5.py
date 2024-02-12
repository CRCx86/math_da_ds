import numpy as np

# Исходные векторы.
A = np.array([1, 2])
B = np.array([3, 4, 5, 6, 7])

print("Исходные векторы:")
print(f"A: {A}")
print()
print(f"B: {B}")
print()

# Склейка двух векторов с указанием axis.
print(np.concatenate([A, B], axis=0))

# Склейка векторов без указания axis (по умолчанию axis=0).
print(np.concatenate([A, B]))

# Склейка в обратном порядке.
print(np.concatenate([B, A]))
