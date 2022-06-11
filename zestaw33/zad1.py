#zad1

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.5, 3*np.pi, 100)
y1 = np.log(2*x)
y2 = 2 * np.cos(x)

plt.plot(x,y1,color="pink",label='-4x + 2', linestyle='dotted')
plt.plot(x,y2,color="orange",label='2cos(x)',linestyle='dashdot')
plt.title('Wykres')
plt.legend()
plt.xlabel('oś x')
plt.ylabel('os y')
plt.grid(True)
plt.savefig('wykres1.png',format='png')
plt.show()