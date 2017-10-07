# k means clustering es un algoritmo sin supervision eso significa
# que no tiene labels, va separar nuestro dataset en categorias de
# una manera aleatoria buscando relaciones de los features

# k es el numero de categorias que vamos a buscar en nuestro
# dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# podemos hacer datasets alatorios con scikitlearn

from sklearn.datasets import make_blobs

data = make_blobs(n_samples=200,n_features=2,centers=4,cluster_std=1.8)

# vamos a graficar para ver los centros que hay

plt.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')
plt.show()

# vamos a entrenar nuestro modelo

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=4)
kmeans.fit(data[0])

# podemos encontrar datos como

print(kmeans.cluster_centers_)
print(kmeans.labels_)

# si esta informacion fuera real hasta aqui termina k means
# pero como sabemos las respuestas podemos comparar resultados

from sklearn.metrics import classification_report

pred = kmeans.labels_
y_test = data[1]

print(classification_report(y_test,pred))

# en este caso no podemos usar classfication report porque k means
# puede interpretar las categorias de otra manera por eso 
# tenemos que graficar resultados

fig,(ax1,ax2) = plt.subplots(1,2,sharey=True,figsize=(10,6))

ax1.set_title('K Means')
ax1.scatter(data[0][:,0],data[0][:,1],c=kmeans.labels_,cmap='rainbow')

ax2.set_title('K Means')
ax2.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')

plt.show()

# k means se usa para intuir los labels no predecirlos, porque es
# un algoritmo sin supervision