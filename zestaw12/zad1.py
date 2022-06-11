
import numpy as np
import matplotlib.pyplot as plt

ticks = ['A', 'B', 'C', 'D', 'E']
colors = ['orange', 'brown', 'purple', 'red', 'blue']
x = np.arange(0, len(ticks))
wyniki = [-47, -27, -24, -15, -50]
plt.barh(x, wyniki, color=colors)
plt.yticks(x, ticks)
plt.title("Wykres Słupki")
plt.show()
