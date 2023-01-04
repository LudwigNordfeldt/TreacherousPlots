import matplotlib.pyplot as mp
import numpy as np

xy = np.linspace(-1, 1)
X,Y = np.meshgrid(xy, xy)
Z = np.arctan(X+Y)*(np.arccos(X) + np.arcsin(Y))

fig = mp.figure()
ax = fig.add_subplot(1, 1, 1, projection = '3d')

fig2 = mp.figure()
ax2 = fig2.add_subplot(1, 1, 1, projection = '3d')
ax2.view_init(145, -60)

fig3 = mp.figure()
ax3 = fig3.add_subplot(1, 1, 1, projection = '3d')
ax3.view_init(145, 60)


p = ax.plot_wireframe(X, Y, Z)
p2 = ax2.plot_wireframe(X, Y, Z)
p3 = ax3.plot_wireframe(X, Y, Z)

mp.show()
