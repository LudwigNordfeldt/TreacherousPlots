import matplotlib.pyplot as mp
import numpy as np

fig, ax = mp.subplots()
ax.set_xlabel("OX")
ax.set_ylabel("OY")
ax.set_title("Convergence")
ax.grid(True)
y = np.linspace(-5, 5)
ax.plot(y, 4*y - 1, 'b-', label = r"$y_1 = 4x - 1 $")
ax.plot(y, 8*y - 5, 'r', label = r"$y_2 = 8x - 5 $")
ax.legend(loc = 0)
ax.text(-4.5, -7.4, r'$ y_1 = 4x - 1$', fontsize = 15, color = 'blue')
ax.text(-4, -40, r'$ y_2 = 8y - 5$', fontsize = 15, color = 'red')
ax.text(-0.3, 10, r'$ x^* = (1,3) $', fontsize = 12, color = 'green')
mp.arrow(-0.3, 9, 1.2, -5, width = 0.1, color = 'green', head_width = 0.3, head_length = 0.45) 
mp.show()
