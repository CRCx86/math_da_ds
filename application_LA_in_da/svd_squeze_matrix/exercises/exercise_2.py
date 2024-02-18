import numpy as np
import matplotlib.pyplot as plt
# Скачивание картинки.
from PIL import Image, ImageOps
import requests

# Ссылка на картинку.
url = "https://code.s3.yandex.net/math-adult/explanations/linal/1/svd/frog.jpeg"

# Скачивание и сохранение картинки в переменную.
im = ImageOps.grayscale(Image.open(requests.get(url, stream=True).raw))
# Превращение картинки в NumPy-массив.
frog = np.array(im).astype(float)


def show_image(img):
    plt.figure(figsize=(12, 8))
    plt.imshow(img, cmap='gray')
    plt.xticks([])
    plt.yticks([])


show_image(frog)

# Ваш код

U, s, VT = np.linalg.svd(frog, full_matrices=False)
S = np.diag(s)

k = 227

U = U[:, 0:k]
S = S[0:k, 0:k]
VT = VT[0:k, :]

X_approx = U @ S @ VT

mse = np.linalg.norm(frog - X_approx) / frog.shape[0] / frog.shape[1]
print(mse)
