import matplotlib.pyplot as mp
import numpy as np

fig, ax = mp.subplots()
ax.set_xlabel("OX")
ax.set_ylabel("OY")
ax.set_title("Parametrically defined function")
ax.grid(True)
t = np.linspace(0, 2*np.pi)
x = t * (t - 2*np.pi)
y = np.sin(t)
ax.plot(x, y, 'b-', label = r"$x(t) = t(t-2\pi); y(t) = sin t$")
ax.legend(loc = 0)

mp.show()
