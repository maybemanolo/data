# en estec aso vamos a hacer un modelo que nos dice si es una flor
# iris dependiendo de los atributos que le pasemos, vamos usar las
# libreria scikit-learn y tensorflow

import tensorflow.contrib.learn as skflow
from sklearn import datasets, metrics

# para usar machine learnign los pasos siempre van a ser, conseguir
# elegir un modelo, entrenar el modelo y probar el modelo

# para nuestra suerte el dataset viene incluido en la libreria
# sklearn, entonces solo la cargamos, pero generalmente se carga el
# dataset de otro archivo como .csv

iris = datasets.load_iris()

# ahora tenemos que elegir un modelo en este caso sera Linear 
# Classifier porque tenemos que hacer un modelo que clasifique entre
# que sea una flor iris o no lo sea

# usamos 3 en n_clases, refiriendono a 3 especies de iris

feature_columns = skflow.infer_real_valued_columns_from_input(iris.data)
classifier = skflow.LinearClassifier(n_classes=3, feature_columns=feature_columns)

# ahora tenemos que entrenar el modelo pasandole los parametros de
# iris.data X y iris.target Y

classifier.fit(iris.data, iris.target)

# vamos a calcular que tan preciso es

score = metrics.accuracy_score(iris.target, clasifier.predict(iris.data))

print("Accuracy "+score)