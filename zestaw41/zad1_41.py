import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0.5,10,50)
Y1 = np.log(2*X)
Y2 = -4*X + 2
Y3 = 2 * np.cos(X)

plt.plot(X,Y1, color='blue', marker='.', label='log(2x)')
plt.plot(X,Y2, color='yellow', marker='>', label = '-4x +2')
plt.plot(X,Y3, color='red', marker = '*', label='2cos(x)')
plt.legend()
plt.title("Wykres")
plt.xlabel("OŚ X")
plt.ylabel("OŚ Y")
plt.grid(True)
plt.savefig("wykres41.png",format='png')
plt.show()

