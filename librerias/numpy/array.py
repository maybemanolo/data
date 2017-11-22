# numpy es es una libreria que hace algebra lineal con python,
# y es sumamente importante porque muchas librerias dependen de
# ell, es muy rapida y tiene enlaces con C

import numpy as np

# nos permite crear numpy arrays que vienen solo de dos maneras
# vectores (1 dimension) y matrices (2 dimensiones)

# tenemos listas normales las cuales son diferentes a los array

my_list = [1,2,3]
# array([1, 2, 3])

# ahora convertimos la lista en array, lo cual la hace en un 

np.array(my_list)

# parece que no movimos nada pero si usamos un lista multi
# dimensional notamos mas

my_mat = [[1,2,3],[4,5,6]]
# array([[1,2,3],
#		 [4,5,6]])

np.array(my_mat)

# tenemos funciones para generar array por ejemplo, np.arange()
# que es como usar una funcio range

np.arange(0,10,2)
# array([0,2,4,6,8,10])

# por ejemplo podmos hacer array de solo ceros, pasandole las
# dimesiones que queremos que tenga con una tupla

np.zeros((2,3))
# array([[0,0,0],
#		 [0,0,0]]

# podemos hacer lo mismo con np.ones()

np.ones((2,3))

# tenemos un metodo llamado np.linspace() el cual lleva 3
# parametros que son primer numero, ultimo y cuantos numero en
# la mitad

np.linspace(0,10,5)
# array([  0. ,   2.5,   5. ,   7.5,  10. ])

# para crear una identity matrix usamos el meotod np.eye() que
# le pasamos un numero, que nos dice las 2 dimensiones del
# matrix, y nos hace una linea en diagonal de 1s y lo demas
# completo de ceros

np.eye(2)
# array([[ 1.,  0.],
#        [ 0.,  1.]])

# tenemos varias maneras para crear un array aleatorio, de los
# metodos mas usados son

# para solo usar una dimension aqui solo pasamos un numero, y 
# para dos no tenemos que pasar una tupla np.random.rand()

np.random.rand(3,2)
# array([[ 0.8747196 ,  0.00225821],
#        [ 0.9986213 ,  0.55600922],
#        [ 0.45273983,  0.12403625]])

# np.random.randn() sirve igual solo que genera numero negativos
# y positivos

np.random.randn(3,2)
# array([[-1.35875732,  0.29439128],
#        [-2.48068166, -0.01072901],
#        [ 0.25847669,  0.53310314]])

# si queremos generar un array de una dimension con numeros 
# aleatorios dentro de un rango usamos el metodo
# np.random.randint()

np.random.randint(1,100,5)
# array([80, 93, 37, 24, 86])

# un metodo muy usado es array.reshape que redefine las
# dimensiones de un array, pero tenemos que usar numero que
# multiplicados den el total de elementos del array mismo

arr = np.random.randint(1,100,10)
arr.reshape(2,5)

# array([[23, 38, 38, 47, 24],
#        [ 9, 13,  1, 45, 35]])

# para econtrar maximo valor del array

arr.max()
# 45

# devuelve la posicion del elemento con mayor valor

arr.argmax()
# 8

# para encontrar el minimo valor del array

arr.min()
# 1

# devuelve la posicion del elemento con menor valor

arr.argmin()
# 7

# para tener la forma de un array

arr.shape()
# (5, 5)

# para saber que tipo de dato hay en un array usamos

arr.dtype
# dtype('int32')