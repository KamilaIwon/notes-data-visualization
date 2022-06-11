import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('ceny33.xlsx')
print(data)

data1 = data[['Rodzaje towarów i usług','Wartosc']]
print(data1.groupby('Rodzaje towarów i usług').mean())

cytryny = data[data['Rodzaje towarów i usług']=='cytryny - za 1 kg']
jablka = data[data['Rodzaje towarów i usług']=='jabłka - za 1kg']
pomarancze = data[data['Rodzaje towarów i usług']=='pomarańcze - za 1kg']


miesiace = jablka['Miesiące']
x = np.arange(0,len(miesiace))
y1 = cytryny['Wartosc']
y2 = jablka['Wartosc']
y3 = pomarancze['Wartosc']

plt.plot(x,y1,color='blue', label='cytryny - za 1 kg')
plt.plot(x,y2,color='green', label='jabłka - za 1kg')
plt.plot(x,y3,color='red', label='pomarańcze - za 1kg')
plt.legend()
plt.xlabel('miesiąc')
plt.ylabel('wartość w zł')
plt.xticks(x,miesiace, rotation=45)
plt.title('Ceny w 2016 roku')
plt.text(1,3,'164933')
plt.show()