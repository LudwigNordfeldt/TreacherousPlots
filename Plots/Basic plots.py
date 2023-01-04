import matplotlib.pyplot as mp
import numpy as np

fig, ax = mp.subplots()
ax.set_xlabel("OX")
ax.set_xticks([-2*np.pi, -3/2*np.pi, -1*np.pi, -1/2*np.pi, 0, 1/2*np.pi, 1*np.pi, 3/2*np.pi, 2*np.pi, 5/2*np.pi, 3*np.pi])
ax.set_xticklabels([r'$-2\pi$', r'$-\frac{3}{2}\pi$', r'$-\pi$', r'$-\frac{1}{2}\pi$', '0', r'$\frac{1}{2}\pi$', r'$\pi$', r'$\frac{3}{2}\pi$', r'$2\pi$', r'$\frac{5}{2}\pi$', r'$3\pi$'])
ax.set_ylabel("OY")
ax.set_title("Sine")
ax.grid(True)
x = np.arange(-2*np.pi, 3*np.pi+1, (5/500*np.pi))
ax.plot(x, np.sin(x), 'b-', label = r"$y = sin(x)$")
ax.plot(x, np.sin(x)**2, 'm-.', label = r"$y = \sin(x)^2$")
ax.legend(loc = 0)


fig, ax2 = mp.subplots()
ax2.set_xlabel("OX")
ax2.set_xticks([x/10.0 for x in range(-2, 104, 8)])
ax2.set_xticklabels(["{:.1f}".format(x/10.0) for x in range(-2, 104, 8)])
ax2.set_ylabel("OY")
ax2.set_title("Exponent")
ax2.grid(True)
x = np.arange(-0.2, 9.4, 9.6/960)
ax2.plot(x, np.exp(-abs(x)), 'r-', label = r"$y = e^{-|x|} $")
ax2.plot(x, 0.01*x**2, 'g-.', label = r"$y = 0.01 x^2$")
ax2.legend(loc = 0)

mp.show()
