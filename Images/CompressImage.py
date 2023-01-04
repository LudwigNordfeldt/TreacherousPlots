import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageEnhance

img = mpimg.imread('Kaiser.jpg')
img2 = Image.fromarray(img)

original_shape = img.shape
image_reshaped = img.reshape((original_shape[0],original_shape[1]*3))

#Complressing (linear decomposition)
imgG = img2.convert('LA')
imgM = np.array(list(imgG.getdata(band = 0)), float)
imgM.shape = (imgG.size[1], imgG.size[0])
imgM = np.matrix(imgM)

u,s,v = np.linalg.svd(image_reshaped)

for i in range(5, 51, 5):
    reconstimg = np.matrix(u[:, :i]) * np.diag(s[:i]) * np.matrix(v[:i, :])
    
plt.imshow(reconstimg, cmap = 'gray')
plt.show()
