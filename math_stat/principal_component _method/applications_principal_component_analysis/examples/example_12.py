from sklearn.datasets import load_digits
from matplotlib import pyplot as plt
import numpy as np

X, y = load_digits(return_X_y=True)
digit = 9
variant = 100
plt.figure(figsize=(4, 4))
plt.imshow(X[y == digit][variant].reshape(8, 8), cmap="Greys")
plt.grid()
plt.yticks(np.arange(0.5, 8), [str(i) + "\\n" * 2 for i in range(1, 9)])
plt.xticks(np.arange(0.5, 8), [str(i) + " " * 9 for i in range(1, 9)])
plt.title(f"Цифра {digit}")
plt.show()
