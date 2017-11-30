# tensorflow es una libreria que nos hace hasta cambiar la forma en que 
# declaramos constantes y variables

import tensorflow as tf

# declaracion de constantes

hello = tf.constant("Hello ")
world = tf.constant("World")

# esto no se puede concatenar e imprimir porque son objetos de tensorflow
# para correr cualquier operacion usamos session

with tf.Session() as sess:
	result = sess.run(hello + world)

print(result)

# tenemos maneras de generar matrices facilmente a partir de funciones

# una matriz de 4x4 de 10s
fill_mat = tf.fill((4,4),10)

# una matriz de 4x4 de ceros
my_zeros = tf.zeros((4,4))

# una matriz de 4x4 unos
my_ones = tf.ones((4,4))

# una matriz de 4x4 aleatoria con un promedio de 0 y una desviacion 
# estandar de 0.5
myrandn = tf.random_normal((4,4),mean=0,stddev=0.5)

# una matriz de 4x4, con valores entre 0 y 1
myrandu = tf.random_uniform((4,4),minval=0,maxval=1)

# los ejecutamos e imprimimos

my_ops = [fill_mat,my_zeros,my_ones,myrandn,myrandu]
a = []

with tf.Session() as sess:
	for i in my_ops:
		a.append(sess.run(i))

for i in a:
	print(i,'\n')

# tambien podemos definir las matrices

mat1 = tf.constant([ [1,2],
					 [3,4] ])

mat2 = tf.constant([[10],[100]])

# podemos ver las dimensiones de una matriz

mat1.get_shape()
mat2.get_shape()

# y hacer operaciones como multiplicacion de matrices

with tf.Session() as sess:
	result = sess.run(mat1 * mat2)

print(result)