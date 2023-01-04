import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageEnhance

img = mpimg.imread('Kaiser.jpg')

# Dark
img2 = Image.fromarray(img)
enhancer = ImageEnhance.Brightness(img2)
factor = 0.4
im_output = enhancer.enhance(factor)

imgplot = plt.imshow(im_output)
plt.show()
