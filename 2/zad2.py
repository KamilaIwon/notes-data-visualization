import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('ceny2.xlsx')
print(data)

data1= data[['Rodzaje towarów','Wartość']]
print(data1)

print(data1.groupby(['Rodzaje towarów']).mean())

a = data[data['Rodzaje towarów']=='ryż - za 1kg']
b = data[data['Rodzaje towarów']=='mąka pszenna - za 1kg']
ryz = a['Wartość']
maka = b['Wartość']
rok = a['Rok']

x = np.arange(0,len(rok))
plt.plot(x,ryz, color='blue', label='ryż za 1 kg')
plt.plot(x,maka, color='green', label='mąka pszenna za 1kg')
plt.legend()
plt.xticks(x,rok)
plt.xlabel('rok')
plt.ylabel('cena w zł')
plt.title('Cena towarów na przestrzeni lat')
plt.annotate('164933', xy=[0.5,2])
plt.savefig('wykres2.jpg', format='jpg')
plt.show()