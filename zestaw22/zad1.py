

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 3* np.pi,50)
y1 = x + np.exp(1)
y2 = -4*x + 2
y3 = np.cos(x)*2

plt.plot(x,y1, color='b', marker='.', label='x + e')
plt.plot(x,y2, color='g', marker='*', label='-4x + 2')
plt.plot(x,y3, color='r', marker='>', label=' 2cos(x)')
plt.title('wykres')
plt.legend()
plt.grid(True)
plt.xlabel('oś X')
plt.ylabel('oś Y')
plt.savefig('zad1.png',format='png')
plt.show()
