# knn es un algoritmo que busca el valor de un nuevo punto 
# dependiendo de que tan cerca o lejos este de unos valores, por
# ejemplo si le damos el valor de k=6 puede que su categoria sea
# una pero si cambiamos el valor de k en el mismo dataset puede
# que la categoria tambien cambie, k es el numero de puntos que 
# tienen que estar cerca para clasifcarlo como de tal categoria

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["patch.force_edgecolor"] = True

df = pd.read_csv('classified_data.csv',index_col=0)

# para este tipo de algoritmo la escala importa mucho lo que vamos
# hacer es estanadrizar todo

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS',axis=1))

scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))

df_feat = pd.DataFrame(scaled_features,columns=df.columns[:-1])

# ahora tenemos nuestro dataset estandarizado

# dividimos el dataset y entrrenamos el modelo

from sklearn.model_selection import train_test_split

X = df_feat
y = df['TARGET CLASS']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)

# ahora hacemos y medimos las predicciones

pred = knn.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,pred))

# en este caso usamos como numero de neighbors 1 y sirve el modelo
# muy bien pero queremos ver de que manera conseguimos un numero
# de neighbor mejor

error_rate = []

for i in range(1,40):
	knn = KNeighborsClassifier(n_neighbors=i)
	knn.fit(X_train,y_train)
	pred_i = knn.predict(X_test)
	error_rate.append(np.mean(pred_i != y_test))

# el metodo de arriba nos va crear una lista con el 
# promedio los valores de los errores cuando usamos cuantos 
# neighbors, ahora solo lo graficamos

plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue')
plt.title('Error vs K')
plt.xlabel('K')
plt.ylabel('Error')
plt.show()

# con la grafica vemos con que numero el error es menos y de ahi
# basamos nuestro numero de k

knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(X_train,y_train)

pred = knn.predict(X_test)
print(classification_report(y_test,pred))