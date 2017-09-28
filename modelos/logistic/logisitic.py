# este es un algoritmo de clasificacion por ejemplo esto se trata
# de detectar si un correo es spam o no, por convencion se usan 2
# clases 1 y 0

# cuando graficamos para logistic regression siempre se usara una
# formula que definira si el valor final sera entre 1 y 0, 
# mientras que el algoritmo decide que va tene de valor, diciendo
# que los valores de 0.5 hace abajo es 0 mientras el resto es 1

# aqui se crea una confusion matrix para ver que tan correcto es
# nuestro modelo logistico

# falso positivo (tipo I) es cuando el modelo predice algo pero
# esta incorrecto y el falso negativo (tipo II) es cuando el 
# modelo predice algo incorrecto

# vamos a predecir si un pasajero del titanic si sobrevive o no

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('titanic_train.csv')

# checamos si hay valores null dentro de nuestro dataset

train.isnull()

# para checar esto es una grafica completamente usamos un heatmap

sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()

# vamos hacer mas visualizaciones al dataset

sns.countplot(x='Sruvived',hue='Sex',data=train)
plt.show()

# una distibucion

sns.distplot(train['Age'].dropna(),kde=False,bins=30)
plt.show()

# informacion

train.info()

# contar hermanos

sns.countplot(x='SibSp',data=train)
plt.show()

# ver cuanta gente pago por boletos caros

train['Fare'].hist(bins=40,figsize(10,4))
plt.show()

# ahora vamos a limpiar nuestro dataset desahaciendonos de los
# valores null o NaN

def impute_age(cols):
	Age = cols[0]
	Pclass = cols[1]
	if pd.isnull(Age): # checa los valores nulos
		if Pclass == 1:
			return 37 # promedio de pclass 1
		elif Pclass == 2:
			return 29 # promedio de pclass 2
		else:
			return 24 # promedio de pclass 3
	else:
		return Age

# usamos axis=1 para aplicar sobre columnas de lo contrario se
# aplicara sobre las filas

train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)

# nos vamos a deshacer de la columna Cabin porque tenemos muy
# poca informacion de esa columna

train.drop('Cabin',axis=1,inplace=True)

# y para terminar con el resto seria

train.dropna(inplace=True)

# vamos a usar unas dummy variables que remplazan strings por
# valores porque un algoritmo no procesa strings

sex = pd.get_dummies(train['Sex'],drop_first=True)

# en este caso tenemos que deshacernos de la primera columna
# ya que al momento que sabemos si alguien es mujer ya sabemos
# que no es hombre entonces nos crea un problema en el algoritmo
# tener una columna que nos diga si es hombre y no es mujer, solo
# dejamos una que diga es mujer o no es mujer

embark = pd.get_dummies(train['Embarked'],drop_first=True)
pclass = pd.get_dummies(train['Pclass'],drop_first=True)

# vamos a agregar estas columnas al dataset

train = pd.concat([train,sex,embark,pclass],axis=1)

# porfin vamos a eliminar las columnas que no nos son utilez

train.drop(['Sex','Embarked','Name','Ticket','PassengerId'],axis=1,inplace=True)

# ahora ya nos toca entrenar un modelo logisitico

X = train.drop('Survived',axis=1)
y = train['Survived']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=101)

from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression()

logmodel.fit(X_train,y_train)

predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report

print(classification_report(y_test,predictions))