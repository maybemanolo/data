# estas son operaciones basicas para usar tensorflow

import tensorflow as tf

# podemos crear constantes

hello = tf.constant('hello world')
x = tf.constant(100)

# vamos a hacer una sesion de tensorflow que es una calse para
# hacer operaciones con las constantes

# un objeto de sesion captura el ambiente donde se hacen las
# operaciones

sess = tf.Session()

# lo corremos con .run() que practicamete solo imprime el valor
# cuando son string pone una b por una indicacion unicode 

sess.run(hello)
sess.run(x)

# si vemos el tipo de datos de esto asi

type(sess.run(hello)) 	# bytes
sess.run(x)				# numpy.int32

# podemos hacer varias operaciones artimeticas abriendo una sesion

x = tf.constant(2)
y = tf.constant(3)

with tf.Session() as sess:
	print('Operation with Constants')
	print('Addition',sess.run(x + y))
	print('Substraction',sess.run(x - y))
	print('Multiplication',sess.run(x * y))
	print('Division',sess.run(x / y))

# tenemos unis objetos llamados placeholder que no tienen un valor,
# simplemente emula que tiene algun tipo que en tensorflow ya estan
# definidos

x = tf.placeholder(tf.int32)
y = tf.placeholder(tf.int32)

# hacemos unas operaciones predefinidas que van a servir casi como a
# funciones en python

add = tf.add(x,y)
sub = tf.subtract(x,y)
mul = tf.multiply(x,y)

# para usarlas cambia un poco la cosa

with tf.Session() as sess:
	print('Operations with Placeholders')
	print('Addition',sess.run(add,feed_dict={x:20,y:30}))
	print('Substraction',sess.run(sub,feed_dict={x:20,y:30}))
	print('Multiplication',sess.run(mul,feed_dict={x:20,y:30}))

# vamos hacer operaciones mas complejas con numpy

import numpy as np

a = np.array([[5.0,5.0]])
b = np.array([[2.0],[2.0]])

# 2 x 5 + 2 x 5 = 20

# los convertimos en info que pueda manejar tensorflow

mat1 = tf.constant(a)
mat2 = tf.constant(b)

# hacemos la operacion/funcion

matrix_multi = tf.matmul(mat1,mat2)

# ejecutamos

with tf.Session() as sess:
	result = sess.run(matrix_multi)
	print(result)