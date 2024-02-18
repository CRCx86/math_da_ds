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
    # plt.show()


# show_image(frog)

# Ваш код
U, s, VT = np.linalg.svd(frog, full_matrices=False)

k = 250

X_approx = U[:, 0:k] * s[0:k] @ VT[0:k, :]
# show_image(X_approx)

result = (len(U[0]) * len(U) + len(s) + len(VT[0]) * len(VT)) * 8 / 1024 / 1024
print(result)
