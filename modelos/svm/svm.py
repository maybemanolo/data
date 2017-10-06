# support vector machine o svm es una linea como en regresion
# lineal, solo que este es un algoritmo de clasificacion, no para
# predecir valores, se pone una linea entre 2 dos categorias y 
# a partir de cierto lado es una categoria, y usamos los puntos
# mas cercanos para poner limites

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# vamos a usar un dataset ya en la libre de scikit learn

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

# asi vemos las llaves de el dataset

cancer.keys()

# para ver la descripcion lo vemos con

cancer['DESCR']

# crear el dataframe

df_feat = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])

# ahora entrenamos el modelo

from sklearn.model_selection import train_test_split

X = df_feat
y = cancer['target']

X_trian, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

from sklearn.svm import SVC

model = SVC()
model.fit(X_trian,y_train)
predictions = model.predict(X_test)

from sklearn.metrics import classification_report

print(classification_report(y_test,predictions))

# tenemos que buscar las mejores parametros con un metodo llamado
# grid search el cual viene incluido en la libreria de sklearn

from sklearn.grid_search import GridSearchCV

# c y gamma son parametros para ajustar la precision

param_grid = {'C':[0.1,1,10,100],'gamma':[0.001,0.01,0.1,1]}

# corremos el gridsearch

grid = GridSearchCV(SVC(),param_grid,verbose=3)
grid.fit(X_trian,y_train)

print(grid.best_params_)
grid_predictions = grid.predict(X_test)

print(classification_report(y_test,grid_predictions))