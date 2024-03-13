from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

X, y = load_diabetes(return_X_y=True)

# random_state необходимо зафиксировать,
# чтобы при каждом запуске разбиение было одинаковым.
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

n_cols = X.shape[1]
pca = PCA(n_cols, random_state=42).fit(X_train)

print(pca.singular_values_)

# Простая визуализация.
plt.bar(range(1, 11), pca.singular_values_)
plt.show()