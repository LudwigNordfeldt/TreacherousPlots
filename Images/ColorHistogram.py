import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageEnhance

img = mpimg.imread('Kaiser.jpg')
img2 = Image.fromarray(img)

histogram = img2.histogram()
HistG = histogram[512:768]
plt.figure(1)
for i in range(0, 256):
    plt.bar(i, HistG[i], color = '#%02x%02x%02x'%(0, i, 0), edgecolor = '#%02x%02x%02x'%(0, i, 0), alpha=0.3)
    
plt.show()
