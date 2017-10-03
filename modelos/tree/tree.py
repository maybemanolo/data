# un decision tree es un algoritmo que sirve como tener muchos if
# y else, para mejorar esto usamos un random forest que mejora
# el rendimiento del algoritmo, esto se usa cuando tenemos una
# feature que influencia mucho el resultado

# https://medium.com/towards-data-science/enchanted-random-forest-b08d418cb411

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('kyphosis.csv')

sns.pairplot(df,hue='Kyphosis')
plt.show()

# vamos a entrenar el modelo

from sklearn.model_selection import train_test_split

X = df.drop('Kyphosis',axis=1)
y = df['Kyphosis']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

# primero un arbol de una decision

from sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier()
dtree.fit(X_train,y_train)

predictions = dtree.predict(X_test)

from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))

# ahora hacemos un random forest

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train,y_train)

rfc_pred = rfc.predict(X_test)
print(classification_report(y_test,rfc_pred))