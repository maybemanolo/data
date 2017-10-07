# pca es principal component analysis, que es un algoritmo para
# hacer una transformacion sobre el dataset que intenta encontrar
# los features que explican mas variana en el dataset, nos 
# deshacemos de los componentes que no explican la mayoria del
# dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.rcParams["patch.force_edgecolor"] = True

# imporamos el dataset de sklearn

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

# esto no es solo el dataframe sino tambien varios componentes que
# lo describen y podemos verlos asi, porque funciona como un
# diccionario

cancer.keys()

# podemos checar la descripicion con

print(cancer['DESCR'])

# creamos nuestro dataframe sin los targets

df = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])

# siempre se hace pca antes de usar un algoritmo para saber que es
# relevante para el target

# ahora standarizamos nuestro dataset

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(df)

scaled_data = scaler.transform(df)

# ahora solo vamos a usar pca

from sklearn.decomposition import PCA

# solo queremos los dos componentes mas importantes de todo el
# dataset

pca = PCA(n_components=2)

pca.fit(scaled_data)

x_pca = pca.transform(scaled_data)

# una vez que ya hicimos pca sobre nuestro dataset lo graficamos
# para ver el efecto

plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer['target'],cmap='rainbow')
plt.xlabel('First PCA')
plt.ylabel('Seconda PCA')
plt.show()

# podemos crear un dataframe a partir de los resultados del pca

df_comp = pd.DataFrame(pca.components_,columns=cancer['feature_names'])
df_comp

# vemos que tan importantes son cada feature con un heatmap,
# mientras mas alto un valor mas relevante

plt.figure(figsize=(12,6))
sns.heatmap(df_comp,cmap='plasma')
plt.xticks(rotation=90)
plt.show()