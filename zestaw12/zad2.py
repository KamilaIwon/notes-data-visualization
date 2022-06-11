
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('sprzedaz12.xlsx')
print(data)

data1 = data[['Produkt', 'Sprzedaż']]
data2 = data1.groupby('Produkt').sum()
print(data2)

data4 = data[data['Produkt'] == 'Marchew']
data5 = data[data['Produkt'] == 'Pomidor']
data6 = data[data['Produkt'] == 'Ogórek']
print(data6)
rok = data4['Rok']
explode = [0, 0.1, 0, 0]
colors = ['purple', 'pink', 'brown', 'red']
plt.subplot(2, 2, 1)
plt.pie(data4['Sprzedaż'], explode=explode, colors=colors, labels=rok, autopct='%1.1f%%')
plt.title("Sprzedaż marchwii", loc='right')
plt.title("164933", loc='left')

plt.subplot(2, 2, 2)
plt.pie(data5['Sprzedaż'], explode=explode, colors=colors, labels=rok, autopct='%1.1f%%')
plt.title("Sprzedaż pomidorów", loc='center')

plt.subplot(2, 2, 3)
plt.pie(data6['Sprzedaż'], explode=explode, colors=colors, labels=rok, autopct='%1.1f%%')
plt.title("Sprzedaż ogórków", loc='center')
# plt.legend()
plt.savefig('wykres2.jpg', format='jpg')
plt.show()
