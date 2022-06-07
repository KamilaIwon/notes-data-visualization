import numpy as np
import matplotlib.pyplot as plt

x = ['A','B','C','D','E']
colors1 = ['lightblue','pink','orange','grey','purple']
colors2 = ['purple','blue','blue','brown','lightgreen']
x1 = np.arange(0,len(x))
y1 = [35, 45, 15, 42, 40]
y2 = [-30, -33, -40, -35, -30]

plt.subplot(1,2,1)
plt.barh(x1,y1, color=colors1)
plt.yticks(x1,x)
plt.title('Wykres lewy')

plt.subplot(1,2,2)
plt.barh(x1,y2, color=colors2)
plt.yticks(x1,x)
plt.title('Wykres prawy')
plt.savefig('wykres1.png',format='png')
plt.show()