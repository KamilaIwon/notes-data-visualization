import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('nieruchomosci2.csv',sep=';', header=None)
data = data.T
data.columns = ['rodzaj','metraz','rok','wartosc']
wartosc = [16266, 37236, 20350, 7369, 33314, 54713, 24121, 10234]
data.drop('wartosc', axis=1, inplace=True)
data['wartość'] = wartosc

pierw = data[data['rodzaj'] == 'rynek pierwotny']
wtorny = data[data['rodzaj'] == 'rynek wtórny']
metraz = pierw['metraz']
explode = [0, 0.1, 0, 0]
colors = ['pink', 'grey', 'purple', 'red']
colors1 = ['yellow', 'orange', 'red', 'pink']

print(pierw)
plt.subplot(2,1,1)
plt.pie(pierw['wartość'], explode=explode, labels=metraz, colors = colors, autopct='%1.1f%%', textprops={'fontsize': 8})
plt.title('rynek pierwotny')
#plt.legend(loc='lower left', prop={'size': 6})
plt.subplot(2, 1, 2)
plt.pie(wtorny['wartość'], explode=explode, labels=metraz, colors = colors1, autopct='%1.1f%%', textprops={'fontsize': 8})
plt.title('rynek wtórny')
plt.savefig('wykres3.pdf', format='pdf')
plt.show()
