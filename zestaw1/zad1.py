
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,50)
y1 = np.sin(x)
y2 = np.cos(x)
yticks = np.linspace(-2,2,9)
fig, ax1 = plt.subplots()
ax1.plot(x,y1,'orange',linestyle='dotted', label='sin(x)')
plt.ylabel('oś lewa',color='green')
plt.xlabel('oś dolna')
plt.legend(loc='center right')
ax2 = ax1.twinx()
ax2.plot(x,y2,'brown',linestyle='dotted', label='cos(x)')
plt.yticks(yticks)
plt.ylabel('oś prawa',color='red')
plt.legend(loc='lower center')
fig.tight_layout()
plt.title("To jest tytuł wykresu")
plt.savefig('wykres1.jpg',format='jpg')
plt.show()