import matplotlib.pyplot as mp
import numpy as np

fig = mp.figure()
ax = fig.add_axes([0.0,0.0, .6, .6], polar = True)
ax.set_xlabel("OX")
ax.set_ylabel("OY")
ax.set_title("Sine")
ax.grid(True)
x = np.linspace(0, 8 * np.pi)
ax.plot(x, np.sin(7*x/4.0), color = 'red', lw = '3', marker = 'o', label = r"$y = sin(7\phi /4)$")
ax.legend(loc = 0)

mp.show()
