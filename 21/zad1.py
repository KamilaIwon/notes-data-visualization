
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 6, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, color='orange', linestyle='dotted', label='sin(x)')
plt.plot(x, y2, color='brown', linestyle='dotted', label='cos(x)')
plt.title('To jest tytuł wykresu')
plt.legend(loc='lower center')
plt.xlabel('oś dolna', color='black')
plt.ylabel('oś lewa', color='green')
plt.show()
