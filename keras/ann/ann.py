# vamos a crear una red neuronal que prediga si una cleinte de
# un banco va cancelar su cuenta en los proximos 6 meses

# primero vamos a preparar la informacion de una manera que
# un algoritmo lo pueda procesar

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importamos el dataset

dataset = pd.read_csv('Churn_Modelling.csv')

# definimos X y Y

X = dataset.drop(['CustomerId','RowNumber','Surname','Exited'],axis=1)
y = dataset['Exited']

# nos deshacemos de los features que son strings

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
gender = le.fit_transform(dataset['Gender'])

geo = pd.get_dummies(dataset['Geography'],drop_first=True)

X = X.drop(['Gender','Geography'],axis=1)
X['Gender'] = gender

X = pd.concat([X,geo],axis=1)

# dividimos el dataset

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

# vamos a establecer todo con una escala standard

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

# ahora creamos la red neuronal

# usamos la libreria de keras que esta encima de tensorflow theanos

import keras
from keras.models import Sequential
from keras.layers import Dense

# inicializamos la ann

classifier = Sequential()

# agregamos layers output y hidden ya que la de input se define desde
# la hidden como veremos

# hidden

classifier.add(Dense(units=6,kernel_initializer='uniform',activation='relu',input_dim=11))

classifier.add(Dense(units=6,kernel_initializer='uniform',activation='relu'))

# output

classifier.add(Dense(units=1,kernel_initializer='uniform',activation='sigmoid'))

# explicacion de los parametros de Dense:

# units: numero de nodes en la hidden layer con unas tecnicas o
# (input_nodes+output_nodes)/2, el seis viene de las 11 columnas de
# X_train mas 1 columna (0 o 1) del ouput dividido entre 2

# kernel_initializer: son valores aleatorios que se le asigna a los weights cerca
# del cero

# activation: es la funcion de activacion que decidimos usar en el
# hidden layer una rectifier function y para el ouput una sigmoid

# input_dim: el numero de nodes del input layer que solo la necesita
# la primera hidden layer ya que las demas sabran que esperar

# sigmoid para logistic en deep learning y si son mas de dos 
# categorias softmax

# compilamos la ann

classifier.compile(optimizer='Adam',loss='binary_crossentropy',metrics=['accuracy'])

# optimizer: la manera en que se van a cambiar los weights, el tipo
# de gradient descent un tipo de esto es adam

# loss: es la funcion de costo que vamos usar, en este caso como
# es logistico (sigmoid) la funcion de ouput usamos binary_crossentropy
# pero si es mas de una categoria es categorical_crossentropy

# metrics: la manera de medir que tan bueno es el modelo

# ahora vamos a entrenar la ann

classifier.fit(X_train,y_train,batch_size=10,nb_epoch=1)

# batch_size: el numero de objetos que quieres que se vean par ajustar
# los weights

# nb_epochs: cuantas veces va checar todo el dataset

# predicciones y precision

y_pred = classifier.predict(X_test)

# tenemos que cambiar las probabilidades a output de 0 y 1 de quien
# se quedo y fue

y_pred = (y_pred > 0.5)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)

from sklearn.metrics import classification_report
ac = classification_report(y_test,y_pred)

print(ac)

# guardamos la red neuronal entrenada

from keras.models import model_from_json

model_json = classifier.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

classifier.save_weights("model.h5")
print("Saved model to disk")

# ahora predecimos un solo valor

# cambiamos los valores de nuestro unico input a los valores que
# usamos para entrenar

arr = np.array([[0.0,0,600,1,40,3,60000,2,1,1,50000]])

# lo estandarizamos

sc.transform(arr)

# predecimos

new_prediction = classifier.predict(arr)
new_prediction = new_prediction > 0.5

print(new_prediction)

# vamos a usar un meotodo llamado kfolds cross validation para
# saber que tan preciso es el modelo, el cual entrena sobre el 90%
# y hace test sobre el otro 10%

# como se usan dos librerias diferentes las importamos por separado

from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score

# hacemos una funcion que construya la red neruonal de arriba

def build_classifier():

	classifier = Sequential()

	classifier.add(Dense(units=6,kernel_initializer='uniform',activation='relu',input_dim=11))
	classifier.add(Dense(units=6,kernel_initializer='uniform',activation='relu'))
	classifier.add(Dense(units=1,kernel_initializer='uniform',activation='sigmoid'))
	classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

	return classifier

# y con esto entrenamos la red

classifier = KerasClassifier(build_fn=build_classifier,batch_size=10,nb_epoch=4)

# aqui es donde aplicamos k folds

accuracies = cross_val_score(estimator=classifier,X=X_train,y=y_train,cv=10,n_jobs=1)

# estimator: es nuestro modelo
# cv: numero de folds del algoritmo, osea cuantas veces los entrenamos
# n_jobs: cuantos cpus usar, -1 es todas

# checamos la accuracy con 

# variance
mean = accuracies.mean()

# bias
variance = accuracies.std()

# dropout regularization es para solucionar overfitting en deep 
# learning

from keras.layers import Dropout

classifier = Sequential()

classifier.add(Dense(units=6,kernel_initializer='uniform',activation='relu',input_dim=11))
classifier.add(Dropout(p=0.1))

classifier.add(Dense(units=6,kernel_initializer='uniform',activation='relu'))
classifier.add(Dropout(p=0.1))

classifier.add(Dense(units=1,kernel_initializer='uniform',activation='sigmoid'))

classifier.compile(optimizer='Adam',loss='binary_crossentropy',metrics=['accuracy'])

classifier.fit(X_train,y_train,batch_size=10,nb_epoch=1)

# para elegir el valor de sera aumentando de 0.1 en 0.1 que es la
# cantidad de neuronas desactivadas

# con esto es con el que vamos a elegir el valor perfecto de batch
# de epochs y mas con parameter tuning

# hyperparametros son los parametros como epochs batch y layers

# vamos a usar una tecnica llamada grid search para optimizar los
# valores de la red neuronal (parameter tuning)

# importamos librerias

from sklearn.model_selection import GridSearchCV

# hacemos una keras classfier con la funcion ya declarada

def build_classifier(optimizer):

	classifier = Sequential()

	classifier.add(Dense(units=6,kernel_initializer='uniform',activation='relu',input_dim=11))
	classifier.add(Dense(units=6,kernel_initializer='uniform',activation='relu'))
	classifier.add(Dense(units=1,kernel_initializer='uniform',activation='sigmoid'))
	classifier.compile(optimizer = optimizer, loss = 'binary_crossentropy', metrics = ['accuracy'])

	return classifier

classifier = KerasClassifier(build_fn=build_classifier)

# creamos diccionario de los hyperparametros con sus posibles valores

parameters = {"batch_size":[25,32],
			"nb_epoch":[100,500],
			"optimizer":['adam','rmsprop']}

# para usar poder cambiar el valor del optimizer tuvimos que agregarlo
# como un parametro a la funcion que construye la red

# ahora implementamos gridsearchcv

grid_search = GridSearchCV(estimator=classifier,param_grid=parameters,scoring='accuracy',cv=10)

grid_search.fit(X_train,y_train)

# buscamos los mejores parametros y ver la precision asi

best_parameters = grid_search.best_params_
best_accuracy = grid_search.best_score_