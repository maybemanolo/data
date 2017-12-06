# vamos a hacer unas operaciones que se hacen en redes neuronales

import numpy as np
import tensorflow as tf

# hacemos seeds de np y tf

np.random.seed(101)
tf.set_random_seed(101)

# creamos nuestros datos aleatoriamente

rand_a = np.random.uniform(0,100,(5,5))
rand_b = np.random.uniform(0,100,(5,1))

# creamos placeholders

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

# creamos operaciones

add_op = a + b
mul_op = a * b

# corremos todo

with tf.Session() as sess:
	add_result = sess.run(add_op,feed_dict={a:rand_a,b:rand_b})
	mult_result = sess.run(mul_op,feed_dict={a:rand_a,b:rand_b})

print(add_result,'\n',mult_result)