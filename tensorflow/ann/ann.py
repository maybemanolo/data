# vamos a ver crear una red neuronal

import tensorflow as tf
import numpy as np

# definimos variables

n_features = 10
n_dense_neurons = 3

# creamos placeholders y variables

x = tf.placeholder(tf.float32,(None,n_features))
W = tf.Variable(tf.random_normal([n_features,n_dense_neurons]))
b = tf.Variable(tf.ones([n_dense_neurons]))

# definimos las operaciones

xW = tf.matmul(x,W)
z = tf.add(xW,b)

# usamos una funcion de activacion

act = tf.sigmoid(z)

# iniciamos todo y ejecutamos

init = tf.global_variables_initializer()

with tf.Session() as sess:

	sess.run(init)

	layer_out = sess.run(act,feed_dict={x:np.random.random([1,n_features])})

# este no es una red neuronal completa ya que no hay
# backpropagation para actualizar los pesos

# regression ejemplo

# creamos nuestros datos

x_data = np.linspace(0,10,10) + np.random.uniform(-1.5,1.5,10)
y_label = np.linspace(0,10,10) + np.random.uniform(-1.5,1.5,10)

# graficamos pare ver nuestra info

import matplotlib.pyplot as plt
plt.plot(x_data,y_label)
plt.show()

# con los nuevos datos ahora vamos a crear una red
# neuronal, vamos a crear una linea que se ajuste a
# los datos hecha con y = mx + b

# primero elegimos dos valores aleatorios para las
# variables m y b

val = np.random.rand(2)

# elegimos aleatorios porque el optimizer nos va
# ajustar los valores en el futuro

m = tf.Variable(val[0])
b = tf.Variable(val[1])

# usamos una funcion de costo

error = 0

for x,y in zip(x_data,y_label):
	y_hat = m*x + b
	error += (y - y_hat)**2

# creamos un optimizador

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
train = optimizer.minimize(error)

# inicializamos todo

init = tf.global_variables_initializer()

# corremos la red

with tf.Session() as sess:

	sess.run(init)
	training_steps = 1

	for i in range(training_steps):
		sess.run(train)

	final_slope, final_intercept = sess.run([m,b])

# evaluamos resultados

x_test = np.linspace(-1,11,10)
y_pred_plot = final_slope * x_test + final_intercept

plt.plot(x_test,y_pred_plot,'r')
plt.plot(x_data,y_label)
plt.show()
