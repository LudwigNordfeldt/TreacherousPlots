import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageEnhance

img = mpimg.imread('Kaiser.jpg')
img2 = Image.fromarray(img)

#Removing green color
img3 = img.copy()
img3[:,:,1] = 0

imgplot = plt.imshow(img3)
plt.show()
