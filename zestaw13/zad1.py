import matplotlib.pyplot as plt


data = [17.4,29.7,17.4,17.4,18.1]
colors = ['royalblue','darkturquoise','darkred','grey','darkorange']
explode = [0,0,0.1,0,0]
lab = ['E','A','B','C','D']
plt.pie(data, colors= colors, explode=explode, labels=lab, autopct='%1.1f%%', shadow=True)
plt.title('Tytuł W')
plt.show()