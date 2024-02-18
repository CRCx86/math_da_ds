# Рабочий код
import numpy as np

a = np.array([
    [3, -9],
    [1, 9]
])

c = a.T @ a
c_vals, c_vecs = np.linalg.eig(c)

# Сортируем собственные значения.
indices = np.argsort(c_vals)  # Считаем индексы, упорядоченные по возрастанию.
indices = indices[::-1]  # "Переворачиваем", чтобы сделать сортировку по убыванию.
# Сортируем собственные значения (= берём их по отсортированным индексам).
c_vals = c_vals[indices]
# Сортируем собственные векторы (здесь [:, indices], потому что сортируем столбцы, а не строки).
V = c_vecs[:, indices]

S = np.diag(np.sqrt(c_vals))

U = a @ V @ np.linalg.inv(S)  # Считаем U по выведенной формуле.

print("Левые сингулярные векторы:")
print(U)
print("Проверка:")
print((U @ S @ V.T).round())  # Округляем до целых.