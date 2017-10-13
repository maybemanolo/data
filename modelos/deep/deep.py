# vamos a hacer una red neuronal que puede analizar numeros a mano
# y saber que numero es, usamos el dataset de MNIST

import tensorflow as tf

# importamos el dataset

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data",one_hot=True)

# checamo el contenido de nuestro dataset

type(mnist)
mnist.train.images.shape

# si checamos un elemnento del dataset vemos que es un array donde
# la mayoria son ceros y el numero que haya es que tan oscura es
# esa parte

mnist.train.images[2]

# tenemos que regresar a la figura a las dimensiones que son
# originalmente, vemos que hay 784 de y y si sacamos la raiz
# cuadrad nos da 28, osea que la figura es de 28x28 y cambiamos la
# forma del array a esa

sample = mnist.train.images[12].reshape(28,28)

# esta forma ya la podemos graficar

import matplotlib.pyplot as plt

# tenemos una funcion que nos permite reconstruir imagenes con los
# arrays que tenemos

plt.imshow(sample,cmap='Greys',interpolation='gaussian')
plt.show()

# ahora vamos a hacer una red neuronal que tome la informacion de
# los arrays e identifique que numero es

# vamos a declarar variables/parametros que siempre vamos a usar
# para una red neuronal

learning_rate = 0.001 	# velocidad de aprendizaje
training_epochs = 15	# ciclos de entranamientos
batch_size = 100		# el tamaños dela info en la que entrenamos

# ahora otros que definin en si la red

n_classes = 10	# 10 posibles outputs (0-9)
n_samples = mnist.train.num_examples	# numero de imagenes
n_input = 784	# numero de pixeles de cada imagen

# ahora configuramos el numero de neuronas que queremos

n_hidden_1 = 256
n_hidden_2 = 256

# 256 es un valor comun cuando usamos imagenes viene de la 
# manera que las computadoras guardan informacion de imagenes
# 8-bit storage

# ahora nos toca hacer nuestra funcion de perdida que nos hace
# ver que tan bien esta nuestra red neuronal, nos notifica de
# cuantos clasificaciones han estado bien

# es para optimizar el modelo

# la optimizacion se aplica tan seguido como se indique en la
# variable learning_rate mientras mas pequeño el valor mas veces
# se va aplicar 

# vamos a hacer un nuestro layer escondidas

def multilayer_perceptron(x,weights,biases):
	
	# X * W + B

	layer_1 = tf.add(tf.matmul(x,weights['h1']),biases['b1'])
	
	# Func(X * W + B) = RELU
	# tf.nn.relu() es nuestra funcion de activacion que realmente
	# solo regresa x o cero

	layer_1 = tf.nn.relu(layer_1)

	# hacemos lo mismo con el segundo layer

	layer_2 = tf.add(tf.matmul(layer_1,weights['h2']),biases['b2'])
	layer_2 = tf.nn.relu(layer_2)

	# al final el ouput

	out_layer = tf.matmul(layer_2,weights['out'] + biases['out'])
	return out_layer

# tenemos otro tipo de dato en tensorflow que es la variable, es
# tensor que se puede cambiar de valor

# ahora necesitamos crear nuestros weights y biases

weights = {
	'h1' : tf.Variable(tf.random_normal([n_input,n_hidden_1])),
	'h2' : tf.Variable(tf.random_normal([n_hidden_1,n_hidden_2])),
	'out': tf.Variable(tf.random_normal([n_hidden_2,n_classes])),
}

biases = {
	'b1' : tf.Variable(tf.random_normal([n_hidden_1])),
	'b2' : tf.Variable(tf.random_normal([n_hidden_2])),
	'out': tf.Variable(tf.random_normal([n_classes])),
}

x = tf.placeholder('float',[None,n_input])
y = tf.placeholder('float',[None,n_classes])

# ahora ya podemos hacer nuestras predicciones

pred = multilayer_perceptron(x,weights,biases)

# ahora hacemos nuestra funcion de costo para optimizacion

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred,y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# ya solo falta entrenar nuestro modelo, asi que iniciamos
# una sesion

sess = tf.InteractiveSession()

# inicializamos nuestras variables que no se hacen cuando se
# declaran sino con run

init = tf.global_variables_initializer()
sess.run(init)

# vamos a entrenar el modelo

for epoch in range(training_epochs):

	avg_cost = 0.0
	total_batch = int(n_samples/batch_size)

	for i in range(total_batch):

		batch_x,batch_y = mnist.train.next_batch(batch_size)
		_,c = sess.run([optimizer,cost],feed_dict={x:batch_x,y:batch_y})

		avg_cost += c/total_batch

	print("Epoch: {} cost{:.4f}".format(epoch+1,avg_cost))

print("model has completed {} epochs of training".format(training_epochs))

# evaluamos el modelo

correct_predictions = tf.equal(tf.argmax(pred,1),tf.argmax(y,1))
correct_predictions = tf.cast(correct_predictions,'float')
accuracy = tf.reduce_mean(correct_predictions)

print(accuracy.eval({x:mnist.test.images,y:mnist.test.labels}))