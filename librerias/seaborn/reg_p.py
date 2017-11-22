import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

# para graficar de manera de regression usamos el siguiente
# metodo, se usan los mismos parametros

sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')
plt.show()

# este es un modelo de regresion, podemos regresar con dos
# graficas pero con resultados diferentes sobre un resultado
# en lugar de usar hue usamos col

sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')
plt.show()

# podemos usar row para ver aun mas combinaciones con el
# dataset

sns.lmplot(x='total_bill',y='tip',data=tips,col='sex',row='time')
plt.show()
