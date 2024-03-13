from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [5, 12],
    [2, 5],
    [0, 2],
    [2, 10],
    [6, 25],
    [3, 14],
    [2, 12],
    [3, 23],
    [7, 26],
    [2, 16]
])

# Создаём объект PCA
pca = PCA(n_components=1)

# Сжимаем данные.
data_compressed = pca.fit_transform(data)

# Строим собственный вектор, на который проецировались данные
# Последний множитель помогает в красивой отрисовке
magnificent_coef = 3
principal_vector = pca.components_[0] * np.sqrt(pca.explained_variance_) * magnificent_coef

# Рассчитываем координаты точек для визуализации главной компоненты
x_min = pca.mean_[0] - principal_vector[0]
x_max = pca.mean_[0] + principal_vector[0]

y_min = pca.mean_[1] - principal_vector[1]
y_max = pca.mean_[1] + principal_vector[1]

plt.figure(figsize=(18, 9))

cmap = "viridis"  # Задаём цветовую схему

# Строим график с исходными данными
plt.subplot(121)
# Исходные данные.
plt.scatter(data[:, 0], data[:, 1], c=data_compressed.flatten(), cmap=cmap, s=100)
# Соответствующие точки на оси
points_on_line = pca.inverse_transform(data_compressed)
# Отрезки между точками и осью
plt.plot(
    np.stack([data[:, 0], points_on_line[:, 0]], axis=1).T,
    np.stack([data[:, 1], points_on_line[:, 1]], axis=1).T,
    zorder=-2,
    linewidth=2,
    c="black",
)
# Визуализируем главную ось
plt.plot(
    [x_min, x_max],
    [y_min, y_max],
    linewidth=3,
    zorder=-2,  # Размещаем линию под точками
    label="Ось главной компоненты",
)
# Задаём формат графика.
plt.xlim(-10, 15)
plt.ylim(-2, 30)
# Делаем отсечки на осях одинаковыми по масштабу
plt.gca().set_aspect("equal")
plt.legend()
plt.title("Исходные данные")

# Строим график со сжатыми данными
plt.subplot(122)
# Трансформированные данные
plt.scatter(
    data_compressed,
    np.zeros(data_compressed.shape),
    c=data_compressed,
    cmap=cmap,
    s=100,
)
# Главная ось.
plt.plot(
    [-20, 20],
    [0, 0],
    zorder=-2,  # Размещаем линию под точками
    linewidth=2,
    label="Ось главной компоненты",
)
# Задаём формат графика.
plt.xlim(-15, 15)
plt.ylim(-10, 10)
# Делаем отсечки на осях одинаковыми по масштабу
plt.gca().set_aspect("equal")
plt.yticks([])  # Отключаем засечки на оси Oy
plt.title("Трансформированные данные")

plt.legend()

plt.show()