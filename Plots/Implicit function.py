import matplotlib.pyplot as mp
import numpy as np

fig, ax = mp.subplots()
ax.set_xlabel("OX")
ax.set_ylabel("OY")
ax.set_title("Implicit function")
ax.grid(True)
x = np.linspace(-3, 3)
y = np.linspace(-3, 3)
X,Y = np.meshgrid(x,y)
F = (X*X + Y*Y)**2 - 7*(X*X - Y*Y)
mp.contour(X, Y, F)
ax.text (-0.96, 1.5, r"$ (x^2 + y^2)^2 - 7(x^2 + y^2)$", color = 'red', fontsize = 12)

mp.show()
