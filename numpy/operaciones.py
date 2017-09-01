# podemos hacer operaciones a arrays con numpy

import numpy as np

arr = np.arange(0,11)

# cuando hacemos operaciones aritmeticas con los arrays 
# de numpy, por ejemplo multiplicar un array con otro, 
# se multiplica cada elemento para hacer otro array

arr + arr
# array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20])

arr - arr
# array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

arr * arr
# array([  0,   1,   4,   9,  16,  25,  36,  49,  64,  81, 100])

arr / arr
# array([ nan,   1.,   1.,   1.,   1.,   1.,   1.,   1.,   1.,   1.,   1.])

# se nota que cuando hacemos la division, el primer valor
# es nan porque estamos dividiendo 0 entre 0 lo cual, daria
# un error si no fuera numpy, aqui da el error pero no para
# el proceso, sino pone nan

# no podemos realizar operaciones con diferentes numeros de
# elementos, pero si podemos multiplicar un array con
# numero, el cual va multiplicar cada elemento

# operaciones matematicas

np.sqrt(arr) 	# raiz cuadrada
np.exp(arr)		# exponencial
np.max(arr)		# maximo valor
np.sin(arr)		# sin
np.log(arr)		# log
arr.sum()		# suma de todos los valores

# se pueden encontrar mas de estas operaciones aqui
# https://docs.scipy.org/doc/numpy-1.13.0/reference/ufuncs.html