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

# units: numerode nodes en la hidden layer con unas tecnicas o
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

classifier.fit(X_train,y_train,batch_size=10,nb_epoch=100)

# batch_size: el numero de objetos que quieres que se vean par ajustar
# los weights

# nb_xwepochs: cuantas veces va checar todo el dataset

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