
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
plt.legend(loc='upper center')
plt.ylabel('Wyniki')
plt.xlabel('Czas')
plt.grid(True)
plt.annotate('164933',xy=[0,30])
plt.savefig('wykres3.png',format='png')
plt.show()
