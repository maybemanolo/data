# el meotod tree.DecisionTreeClassifier() te permite crear un 
# decision tree, es un arbol con multiples preguntas, mientras la 
# respuesta sea si va de un lado y si es no va del otro hasta 
# llegar a un valor despues de varias preguntas

from sklearn import tree

clf = tree.DecisionTreeClassifier()

# tenemos este dataset, el label x es una lista de listas con los
# datos de el altura anchura y talla de zapato de un persona,
# mientras que el label y y tiene el genero de la persona

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], 
	 [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], 
	 [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 
	 'female','female', 'male', 'male']

# el metodo clf.fit() entrena nuestro decision tree

clf = clf.fit(X, Y)

# el metodo clf.predict predice que valor Y es mas probable que tenga
# dependiendo que valores X pasamos

pred_tree = clf.predict(X)
prediction_tree = clf.predict([[190, 70, 43]])

print(prediction_tree)

## Reto

# modelo 1 K Nearest Neighbor

from sklearn import neighbors

clf_knn = neighbors.KNeighborsClassifier()
clf_knn.fit(X,Y)

pred_knn = clf.predict(X)
prediction_knn = clf.predict([[190, 70, 43]])
print(prediction_knn)

# modelo 2 Support Vector Machine

from sklearn import svm

clf_svc = svm.SVC()
clf_svc.fit(X,Y)

pred_svc = clf_svc.predict(X)
prediction_svc = clf_svc.predict([[190, 70, 43]])
print(prediction_svc)

# modelo 3 Random Forest

from sklearn import ensemble

clf_rf = ensemble.RandomForestClassifier()
clf_rf.fit(X,Y)

pred_rf = clf_rf.predict(X)
prediction_rf = clf_rf.predict([[190, 70, 43]])
print(prediction_rf)

# podemos usar accuracy_score para saber que tan exacto es nuestro
# modelo que lleva como parametros Y label y predict

from sklearn.metrics import accuracy_score

acc_tree = accuracy_score(Y, pred_tree) * 100
acc_knn = accuracy_score(Y, pred_knn) * 100 
acc_svc = accuracy_score(Y, pred_svc) * 100 
acc_rf = accuracy_score(Y, pred_rf) * 100

print("Decision Tree: "+ str(acc_tree))
print("K Nearest Neighbor: "+ str(acc_knn))
print("Support Vector Machine: "+ str(acc_svc))
print("Random Forest: "+ str(acc_rf))