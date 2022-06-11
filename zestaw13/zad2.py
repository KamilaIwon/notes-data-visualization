import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_excel('ceny13.xlsx')
print(data)

data1=data[['Rodzaje towarów','Wartosc']]

print(data1)
print(data1.groupby('Rodzaje towarów').mean())

dzem = data[data['Rodzaje towarów']=='dżem - za 360g']
miod = data[data['Rodzaje towarów']=='miód pszczeli - za 400g']

rok = dzem['Rok']
x = np.arange(0,len(rok))
fig, ax1 = plt.subplots()

ax1.plot(x, dzem['Wartosc'], color = 'deeppink', label='dżem - za 360g')
plt.legend()
ax2 = ax1.twinx()
plt.plot(x, miod['Wartosc'], color= 'royalblue',label='miód pszczeli - za 400g')
plt.xticks(x,rok)
plt.legend()
plt.xlabel('Rok')
plt.ylabel('Wartość w zł')
plt.title('Wartość dżemu oraz miodu na przestrzeni lat')
plt.show()