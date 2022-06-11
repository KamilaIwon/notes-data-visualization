import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('cechy33.csv', sep=';', decimal=',')
print(data)

x = np.arange(0,4,1)
a = data['Cecha1']
b = data['Cecha2']
cats1 = pd.cut(a,[0,50,100,150,200],right=True)
cats2 = pd.cut(b,[0,50,100,150,200],right=True)


data2 = pd.value_counts(cats1)
data3 = pd.value_counts(cats2)
print(data2)
x3 = ['[100, 150)', '[0, 50)', '[150, 200)', '[50,100)']

plt.barh(x,data2,label='cecha1', height=0.3)
plt.barh(x+0.3,data3,label='cecha2', height=0.3)
plt.legend()
plt.title('wykres')
plt.yticks(x+0.15,x3)
plt.show()