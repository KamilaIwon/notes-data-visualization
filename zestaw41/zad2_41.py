import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("ceny41.xlsx")
print(data)

a = data[['Rodzaje towarów i usług','Wartosc']]
a = a.groupby(['Rodzaje towarów i usług']).mean()

b = data[data['Rodzaje towarów i usług']=='marchew - za 1 kg']
c = data[data['Rodzaje towarów i usług']=='cebula - za 1 kg']
d = data[data['Rodzaje towarów i usług']=='ziemniaki - za 1 kg']
print(b)

miesiace = b['Miesiące'].tolist()
print(miesiace)

X = np.arange(0,len(miesiace))
print(X)
marchewki = b['Wartosc']
cebula = c['Wartosc']
ziemniaki = d['Wartosc']

plt.plot(miesiace,marchewki,label='Marchew')
plt.plot(miesiace,cebula,label='Cebula')
plt.plot(miesiace,ziemniaki,label='Ziemniaki')
plt.title("Wartość warzyw w 2017 roku")
plt.ylabel("Wartość w zł")
plt.xlabel("Miesiące")
plt.xticks(X,miesiace,rotation=45)
plt.legend()
plt.annotate(xy=[1, 1], text='164933')
plt.savefig('wykresceny.jpg',format='jpg')
plt.show()