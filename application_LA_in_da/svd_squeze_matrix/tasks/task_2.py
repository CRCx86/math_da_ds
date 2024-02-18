import numpy as np
import matplotlib.pyplot as plt
# Скачивание картинки.
from PIL import Image, ImageOps
import requests

# Ссылка на картинку.
url = "https://code.s3.yandex.net/Math/images/carpet.jpeg"

# Скачивание и сохранение картинки в переменную.
im = ImageOps.grayscale(Image.open(requests.get(url, stream=True).raw))
# Превращение картинки в NumPy-массив.
carpet = np.array(im).astype(float)


def show_image(img):
    plt.figure(figsize=(12, 8))
    plt.imshow(img, cmap='gray')
    plt.xticks([])
    plt.yticks([])
    plt.show()


show_image(carpet)

# Ваш код
U, s, VT = np.linalg.svd(carpet, full_matrices=False)
S = np.diag(s)

k = 10

U = U[:, 0:k]
S = S[0:k, 0:k]
VT = VT[0:k, :]

X_approx = U @ S @ VT

mse = np.linalg.norm(carpet - X_approx) / carpet.shape[0] / carpet.shape[1]
print(mse)
