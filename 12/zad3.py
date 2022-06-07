
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('dosw12.csv', sep=';', decimal=',')

data = data.dropna()

y1 = data['Zmienna1']
y2 = data['Zmienna2']
y3 = data['Zmienna3']
x = data['Czas']

plt.plot(x, y1, color='red', label='Zmienna 1')
plt.plot(x, y2, color='blue', label='Zmienna 2')
plt.plot(x, y3, color='green', label='Zmienna 3')
plt.title('Wykres')
plt.legend()
plt.ylabel('Wyniki')
plt.xlabel('Czas')
plt.grid(True)
plt.savefig('Wykres3.png',format='png')
plt.show()
