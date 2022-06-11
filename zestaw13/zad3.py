import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('turystyka13.csv', sep=';', header=None)
data = data.T
data.columns=['rodzaj','Rok','Kategoria','Ilosc']
ilosc = [2540,2592,110,110,384,420]
data.drop('Ilosc', axis=1, inplace=True)
data['Ilość']=ilosc
print(data)

hotel = data[data['rodzaj']=='hotele']
motel = data[data['rodzaj']=='motele']
pensjonat = data[data['rodzaj']=='pensjonaty']
rok = hotel['Rok']
x = np.arange(0,len(rok))
plt.bar(x, hotel['Ilość'], color='green', width=0.25, label='hotele')
plt.bar(x+0.25, motel['Ilość'], color='blue', width=0.25, label='motele')
plt.bar(x+0.5, pensjonat['Ilość'], color='orange', width=0.25, label='pensjonaty')
plt.xticks(x+0.25,rok)
plt.legend()
plt.xlabel('Rok')
plt.ylabel('Ilość')
plt.title('Wykres3')
plt.show()
