
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_excel('sprzedaz21.xlsx')
print(data)

data1 = data[['Produkt','Sprzedaż']]
print(data1.groupby('Produkt').sum())

a = data[data['Produkt']=='Marchew']
b = data[data['Produkt']=='Pomidor']
c = data[data['Produkt']=='Ogórek']
print(a)

miesiace = a['Rok']
x = np.arange(0,len(a['Rok']),1)
marchew = a['Sprzedaż']
pomidor = b['Sprzedaż']
ogorek = c['Sprzedaż']

plt.barh(x+0.0,marchew, height=0.2,label='marchew')
plt.barh(x+0.25,pomidor,height=0.2, label='pomidor')
plt.barh(x+0.5,ogorek,height=0.2, label='ogórek')
plt.yticks(x+0.25,miesiace)
plt.ylabel('Rok')
plt.xlabel('Sprzedaż')
plt.legend()
plt.title('Sprzedaż warzyw w latach 2015-18')
plt.savefig('wykres2.jpg',format='jpg')
plt.show()