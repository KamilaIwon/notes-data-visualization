
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data1 = pd.read_csv('transport22.csv', sep=';', index_col=None)
data2 = data1.T

# wykonane kroki:
# importowanie danych
# odwrocenie tabeli
# dodanie kolumny ID
# zamienić kolumne id na index
# dodac kolumne pojazdy poprzez insert
# zamienic nazwy kolumn na poprawne
# pogrupowanie przez pojazdy i lata
# utworzenie wykresów
# zapisanie i wywołanie wykresów


data2['ID'] = np.arange(0, 21, 1)
data2.set_index('ID', inplace=True)

pojazdy = ['motocykle ogolem', 'motocykle ogolem', 'motocykle ogolem', 'motocykle ogolem', 'motocykle ogolem', 'motocykle ogolem', 'motocykle ogolem',
         'samochody osobowe', 'samochody osobowe','samochody osobowe', 'samochody osobowe', 'samochody osobowe','samochody osobowe', 'samochody osobowe',
         'autobusy ogółem', 'autobusy ogółem', 'autobusy ogółem', 'autobusy ogółem', 'autobusy ogółem', 'autobusy ogółem', 'autobusy ogółem']

data2.insert(0, 'pojazd', pojazdy)
data2.columns = ['pojazd', 'rok', 'jednostka', 'ilość']


data3 = data2.groupby(['pojazd', 'rok']).sum()

d = data2[data2['rok'] == '2010']
rok2010 = [1013014, 17239800, 97044]

print(d)

plt.pie(rok2010, labels=['motocykle ogółem', 'samochody osobowe', 'autobusy ogółem'])
plt.title('rok 2010')
plt.title('164933', loc='right')
plt.legend(loc='lower right')
plt.savefig('rok2010.jpg',format='jpg')
plt.show()

e = data2[data2['rok'] == '2015']
print(e)
rok2015 = [1272333, 20723423, 109844]
plt.pie(rok2015, labels=['motocykle ogółem', 'samochody osobowe', 'autobusy ogółem'])
plt.legend(loc='lower left')
plt.title('rok 2015')
plt.savefig('rok2015.jpg',format='jpg')
plt.show()

