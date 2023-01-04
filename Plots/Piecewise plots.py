import matplotlib.pyplot as mp
import numpy as np

fig, ax = mp.subplots()
ax.set_xlabel("OX")
ax.set_ylabel("OY")
ax.set_title("Piecewise")
ax.grid(True)
x1 = np.arange(-2, 1, 0.05)
x2 = np.arange(1, 3, 0.05)
x3 = np.arange(3, 8, 0.05)
ax.plot(x1, (x1-1)**2, 'g-.', label = r"$y = (x-1)^2$")
ax.plot(x2, np.cos(np.pi/2 * x2), 'b-', label = r"$y = cos(\frac{\pi}{2}x)$")
ax.plot(x3, 1 - np.exp(3-x3), 'm', label = r"$y = 1 - e^(3-x)$")
ax.legend(loc = 0)

mp.show()
