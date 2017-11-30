# las graficas (graphs) son hechas detras del codigo, conectan nodos los cuales
# son operaciones con posibles entradas para una salida

import tensorflow as tf

# construimos una grafica que suma dos numeros

n1 = tf.constatnt(1)
n1 = tf.constatnt(2)
n3 = n1 + n2

with tf.Session() as sess:
	result = sess.run(n3)

print(result)

# en realidad estas se crean por default no las tenemos que definir siempre
# pero podemos crear extras 

# hace referancia a mi grafica hecha por default
graph_one = tf.get_default_graph()

# creamos una grafica extra
graph_two = tf.Graph()

with graph_two.as_default():
	print(graph_two is tf.get_default_graph())