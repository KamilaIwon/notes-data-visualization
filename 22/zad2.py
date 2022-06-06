
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# zaladuj plik

data = pd.read_excel('mieszkania22.xlsx')
print(data)

# wyświetl na konsoli średnią z poszczególnych lat

srednia = data.groupby(['Formy budownictwa','Rok']).mean()
print(srednia)
data1 = data[['Formy budownictwa','Wartość']]
print(data1.groupby(['Formy budownictwa']).mean())

x = 4
a = data[data['Rok']==2015]
b = data[data['Rok']==2016]
c = data[data['Rok']==2017]
d = data[data['Rok']==2018]

rok2015 = a['Wartość'].values.tolist()
rok2016 = b['Wartość'].values.tolist()
rok2017 = c['Wartość'].values.tolist()
rok2018 = d['Wartość'].values.tolist()

data1 = [rok2015,rok2016,rok2017,rok2018]
print(data1)

X = np.arange(3)
#plt.bar(X + 0.00, data1[0], color='b', width=0.2, label="2015")
#plt.bar(X + 0.25, data1[1], color='g', width=0.2, label="2016")
#plt.bar(X + 0.50, data1[2], color='r', width=0.2, label="2017")
#plt.bar(X + 0.75, data1[3], color='yellow', width=0.2, label="2018")
#plt.xticks(X+0.4, ('indywidualne', 'komunalne', 'spółdzielcze'))
#plt.show()



x = 4
a = data[data['Formy budownictwa']=='indywidualne']
b = data[data['Formy budownictwa']=='komunalne']
c = data[data['Formy budownictwa']=='spółdzielcze']


ind = a['Wartość'].values.tolist()
kom = b['Wartość'].values.tolist()
spol = c['Wartość'].values.tolist()

data1 = [ind,kom,spol]
print(data1)

X = np.arange(4)
plt.bar(X + 0.00, data1[0], color='b', width=0.2, label="indywidualne")
plt.bar(X + 0.25, data1[1], color='g', width=0.2, label="komunalne")
plt.bar(X + 0.50, data1[2], color='r', width=0.2, label="spółdzielcze")
plt.xticks(X+0.4, ('2015', '2016', '2017','2018'))
plt.title("Wykres")
plt.title('164933',loc='right')
plt.xlabel('Rok')
plt.ylabel('Wartość')
plt.legend()
plt.show()

#zmieniamy na poziomo

X = np.arange(4)
plt.barh(X + 0.00, data1[0], color='b', height=0.2, label="indywidualne")
plt.barh(X + 0.25, data1[1], color='g', height=0.2, label="komunalne")
plt.barh(X + 0.50, data1[2], color='r', height=0.2, label="spółdzielcze")
plt.yticks(X+0.4, ('2015', '2016', '2017','2018'))
plt.title("Wykres")
plt.title('164933',loc='right')
plt.ylabel('Rok')
plt.xlabel('Wartość')
plt.legend()
plt.savefig('wykres3.pdf',format='pdf')
plt.show()