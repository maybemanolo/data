# tenemos la libreria seaborn que esta basada en metplotlib
# que srive igual para visualizar datos de diferente manera
# o mejor

import matplotlib.pyplot as plt
import seaborn as sns

# tenemos ya datasets en la libreria para visualizar asi que
# importamos una

tips = sns.load_dataset('tips')

# esto nos devuelve un dataset como un dataframe

# una de las maneras de visualizar el dataset es usando el 
# metodo sns.distplot(), a estos metodos no se le pasan
# dataframes sino series

sns.distplot(tips['total_bill'])
plt.show()

# nos muestra esto un histogram con un kde, que es una linea
# que pasa por los valores, lo desactivamos asi

sns.distplot(tips['total_bill'],kde=False)
plt.show()

# podemos modificar la cantidad de bins que son la barras,
# con el parametro bins solo pasando un int, hay que tener
# cuidado con el tamaño del bin

sns.distplot(tips['total_bill'],kde=False,bins=40)
plt.show()

# tenemos un metodos que nos compara dos columnas dentro de
# un dataset

sns.jointplot(x='total_bill',y='tip',data=tips)
plt.show()

# podemos graficar esto de varias maneras con el parametro 
# kind usando: hex, reg, kde

# este otro metodo nos muestra una serie de graficas comparando
# todas las columnas con todas, cuando se compara con si mismo,
# muestra un histogram, y cuando es con otro, es un jointplot()

sns.pairplot(tips)
plt.show()

# si queremos dividir la informacion de cada grafica por otras
# columnas por ejemplo por sexo usamos el parametro hue, se le
# pasa una columa categorial, no que tenga un valor por eso 
# usamos sexo, porque solo se elige hombre o mujer no numeros

sns.pairplot(tips,hue='sex')
plt.show()

# podemos graficar esto solo con el kde solo con pasar una
# columna

sns.kdeplot(tip['total_bill'])