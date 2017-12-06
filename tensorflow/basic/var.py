# vamos a declarar variables y placeholders

import tensorflow as tf
my_tensor = tf.random_uniform((4,4),0,1)

# una variable solo guarda un valor que se puede cambiar en el futuro

my_var = tf.Variable(initial_value=my_tensor)

# tenemos que inicializar las variables siempre

init = tf.global_variables_initializer()

# ejecutamos para asignar los valores de variables

with tf.Session() as sess:
	result = sess.run(init)

print(result)

# podemos hacer placeholders que se usan para darles valores en la etapa de
# entrenamiento, en la formula f(x) = mx + b, x es el placeholder porque se 
# le van a pasar valores despues

# solo se indica el tipo de dato que se pasara en el futuro

ph = tf.placeholder(tf.float32)