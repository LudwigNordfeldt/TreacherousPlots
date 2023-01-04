import matplotlib.pyplot as mp
import numpy as np

a = int (input('Введите сторону равностороннего треугольника: '))
fig = mp.figure()
ax = fig.add_subplot()

f = mp.Polygon ( [ [0, 0], [a * 0.5, a * 0.5 * (3**0.5)], [a, 0] ], color = 'g', alpha = 0.5 )
f2 = mp.Circle ( (a/2, a*3**0.5/6), a*3**0.5/6, color = 'b', alpha = 0.5 )
ax.add_patch(f)
ax.add_patch(f2)
ax.axis('equal')

fig.savefig('triangle.png', dpi = 400)
mp.show()
