import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('cechy41.csv',sep=';', encoding="UTF-8", decimal=',')
print(data)


X = np.arange(0,4,1)
print(len(X))
a = data['Cecha1']
b = data['Cecha2']
print(a)
cats1 = pd.cut(a,[0,50,100,150,200], right=False)
cats2 = pd.cut(b,[0,50,100,150,200], right=False)

data3 = pd.value_counts(cats1)
data4 = pd.value_counts(cats2)
x3 = ['[100, 150)', '[0, 50)', '[150, 200)', '[50,100)']
print(data3)
print(data4)
plt.subplot(2, 2, 1)
plt.barh(X,data3,height=0.25,label='Cecha1')
plt.barh(X+0.25,data4,height=0.25, label='Cecha2')
plt.legend()
plt.yticks(X+0.1, x3)
plt.title("Wykres")


c = a.sum()
d = b.sum()
x = [c,d]
print(x)
plt.subplot(2, 2, 2)
plt.pie(x,labels=['Cecha1', 'Cecha2'])
plt.show()




