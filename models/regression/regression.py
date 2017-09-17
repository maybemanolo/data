# lo primero que vamos a hacer es siempre ver y analizar nuestro
# dataset de primera vista

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# cargarmos el dataset

df = pd.read_csv('USA_Housing.csv')

# checamos cosas importantes con metodos

df.info()
df.describe()
df.columns

# cuando no tenemos un dataset no muy grande usamos pairplot para
# empezar a visualizar

sns.pairplot()
plt.show()

# vamos a intentar predecir el precio de una cassa de acuerdo
# a las cosas que tenga, asi que vemos la distribucion del
# la columna price

sns.distplot(df['Price'])
plt.show()

# checamos la correlacion que hay entre cada una de las columnas

sns.heatmap(df.corr(),annot=True)
plt.show()