import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset('tips')

# podemos categorizar al momento de visualizar los datos con
# los siguientes metodos

# tenemos sns.barplot() que nos muestra dos barras que muestran
# el promedio sobre dos categorias que definimos

# en este caso seria sex las categorias y nos muestra el
# promedio de total_bill

sns.barplot(x='sex',y='total_bill',data=tips)
plt.show()

# si queremos cambiar el tipo de resultado que nos grafique,
# como promedio, standard deviation, max usamos el parametro
# estimator

import numpy as np
sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)
plt.show()

# podemos contar tambien los valores de la columna, pero solo
# damos el valor x porque busca solo las ocurrencias

sns.countplot(x='sex',data=tips)
plt.show()

# podemos graficar de otras maneras, x = categoria, y = valores

sns.boxplot(x='day',y='total_bill',data=tips)set_title("Boxplot")
plt.show()

sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)set_title("ViolinPlot")
plt.show()

sns.stripplot(x='day',y='total_bill',data=tips,jitter=True)set_title("StripPlot")
plt.show()

sns.boxplot(x='day',y='total_bill',data=tips)set_title("SwarmPlot")
plt.show()

sns.factorplot(x='day',y='total_bill',data=tips,kind='bar')set_title("FactorPlot")
plt.show()