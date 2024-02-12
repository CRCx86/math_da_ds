import numpy as np

# Исходные векторы.
A = np.array([1, 2])
B = np.array([3, 4])

print("Исходные векторы:")
print(f"A: {A}")
print()
print(f"B: {B}")
print()

# Склейка по вертикали. Попробуйте изменить строку ниже.
print(np.stack([B, A], axis=1))
