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

sns.pairplot(data=df)
plt.show()

# vamos a intentar predecir el precio de una cassa de acuerdo
# a las cosas que tenga, asi que vemos la distribucion del
# la columna price

sns.distplot(df['Price'])
plt.show()

# checamos la correlacion que hay entre cada una de las columnas

sns.heatmap(df.corr(),annot=True)
plt.show()

# ahora vamos a crear el modelo y hacer predicciones

# vamos a dividir nuestro dataset en diferentes variables como
# X que son los features y Y lo que intentamos predecir de acuerdo
# a los valores de X

X = df[['Avg. Area Income','Avg. Area House Age','Avg. Area Number of Rooms','Avg. Area Number of Bedrooms','Area Population']]

y = df['Price']

# vamos a separar nuestro dataset entre info para entrenar e info 
# para probar

from sklearn.model_selection import train_test_split

# test_size es el procentage de tu dataset que quieres que se
# use para probar las predicciones, y random_state es lo mismo
# que numpy.seed()

X_train, X_test, y_train, y_test = train_test_split(X,y,test_sixe=0.33,random_state=101)

# ahora vamos a importar nuestro linear regression model

from sklearn.linear_model import LinearRegression

lm = LinearRegression()

# vamos a entrenar nuestro modelo con nuestras variables X_train
# y y_train

lm.fit(X_train,y_train)

# ahora vamos a evaluar el modelo, obeteniedo valores como

# intercept

lm.intercept_

# coeficientes, que convertimos en un dataframe

lm.coef_
cdf = pd.DataFrame(lm.coef_, index=X.columns,columns=['Coeff'])

# un coeficiente nos dice que la relacion de un valor de X con
# el valor Y, por ejemplo en el dataset el coeficiente por cada
# unidad que se aumenta a cierta columna se le aumenta cierto
# valor en Y, ese valor es el coeficiente

# vamos hacer predicciones

predictions = lm.predict(X_test)

# para ver cuanta precision tiene nuestro modelo usamos y_test
# que tiene los resultados correctos y predictions que tiene
# nuestras predicciones que vamos a comparar

# lo graficamos y si la grafica nos da un linea perfecta significa
# que el modelo es muy bueno

plt.scatter(y_test,predictions)
plt.show()

# tambien podemos checar el resultado de los residuos que es
# y_test - predictions

sns.distplot((y_test - predictions))
plt.show()

# vamos a usar una funciones especiales para medir el error de
# nuestros modelos

from sklearn import metrics

# usamos los metodos

metrics.mean_absolute_error(y_test,predictions)
metrics.mean_squared_error(y_test,predictions)
np.sqrt(metrics.mean_squared_error(y_test,predictions))

# para saber que tan bien sirve un modelo usamos el siguiente
# metodo, que nos da el porcentaje de cuanto podemos explicar

metrics.explained_variance_score(y_test,predictions)