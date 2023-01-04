import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageEnhance

img = mpimg.imread('Kaiser.jpg')
img2 = Image.fromarray(img)

grayscale_img = img[:, :, 0]
plt.imshow(grayscale_img, cmap='gray')

plt.show()
