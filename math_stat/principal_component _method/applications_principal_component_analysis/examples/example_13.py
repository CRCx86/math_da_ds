from sklearn.datasets import load_digits
from matplotlib import pyplot as plt

X, y = load_digits(return_X_y=True)
plt.figure(figsize=(6, 4))
idxs = [4, 12, 3, 0, 8, 5]
for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.imshow(X[idxs[i - 1]].reshape(8, 8), cmap='Greys')
    plt.xticks([])
    plt.yticks([])
    plt.title(f'Цифра {y[idxs[i - 1]]}')
plt.tight_layout()
plt.show()
