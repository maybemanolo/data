# importamos nuestra libreria

from deep_lb import *

# creamos nuestro dataset

from sklearn.datasets import make_blobs
data = make_blobs(n_samples=50,n_features=2,center=2,random_state=75)

# dividimos los datos

features = data[0]
label = data[1]

# graficamos

import matplotlib.pyplot as plt
plt.scatter(features[:,0],features[:,1],c=label)
plt.show()

# hacemos predicciones manualmente

np.array([1, 1]).dot(np.array([[8],[10]])) - 5
np.array([1,1]).dot(np.array([[4],[-10]])) - 5

# usamos la libreria

g = Graph()
g.set_as_default()

x = Placeholder()
m = Variable([1,1])
b = Variable(-5)

z = add(matmul(w,x),b)
a = Sigmoid(z)

sess = Session()
sess.run(operation=a,feed_dict={x:[8,10]})
sess.run(operation=a,feed_dict={x:[2,-10]})