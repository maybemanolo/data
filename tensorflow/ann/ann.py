# vamos a ver crear una red neuronal

import tensorflow as tf

# definimos variables

n_features = 10
n_dense_neurons = 3

# creamos placeholders y variables

x = tf.placeholer(tf.float32,(None,n_features))
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

	layer_out = sess.run(a,feed_dict={x:np.random.random([1,n_features])})