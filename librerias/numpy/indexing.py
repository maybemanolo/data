# vamos a ver como elegir cierto elementos de un arra

import numpy as np 

# creamos un array

arr = np.arange(0,11)

# igual como si estuvieramos accesando valores de una lista
# usamos brackets y slices asi como

arr[0] 		# 0
arr[-1]		# 10
arr[1:4]	# array([1, 2, 3, 4])
arr[:3]		# array([0, 1, 2])
arr[6:]		# array([6, 7, 8, 9, 10])
arr[:]		# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# podemos cambiar el valor de varios elementos de un array
# usando slices

arr[0:3] = 100
# array([100, 100, 100, 3, 4, 5, 6, 7, 8, 9, 10,])

# para que la memoria se use de lo mejor posible cuando 
# ponemos una slice dentro de una variable, haciendo que
# se haga una referencia no otra variable, ejemplo

arr = np.arange(0,11)
slice_arr = arr[:6]

slice_arr[:] = 99
print(slice_arr)
# array([99, 99, 99, 99, 99, 99])

print(arr)
# array([99, 99, 99, 99, 99, 99, 6, 7, 8, 9, 10])

# para evitar esto es hacer una copia del array con un metod
# ya en el array

arr_copy = arr.copy

# ahora ya podemos hacer cambio a arr_copy sin cambiar el
# valor de arr

# para acceder valores a array de dos dimensiones o una
# matrix

arr_2d = np.arange(0,11)
arr_2d = arr_2d.shape(2,5)
# array([[0, 1, 2, 3, 4],
#        [5, 6, 7, 8, 9]])

# para acceder a cada valor usamos dos bracket [][] para
# especificar cual array dentro del array elegimos y cual
# elemento de ese array queremos

arr_2d[0][1]
# 1

# en lugar de usar doble bracket tambien podemos usar un
# bracket, y poner los dos valores separandolos por una coma

arr_2d[0, 1]
# 1

# si queremos elegir varios valores dentro de un matrix solo
# usamos slices dentro

arr_2d[:1,1:]
# array([[1, 2, 3, 4]])

# podemos hacer operacion logicas y aritmeticas a un array
# pero lo que hace es devolvernos un array con cada elemento
# despues de la operacion, por ejemplo

arr = np.arange(1,11)

# relacional

arr < 5
# array([ True,  True,  True,  True, False, 
#      	False, False, False, False, False], dtype=bool)

# tener esto nos hace seleccionar cosas de una manera
# mas especifica con las condicionales, porque solo nos 
# va regresar el valor donde diga True

# en este ejemplo traemos todos los numeros menores a 5

arr[arr < 5]
# array([1, 2, 3, 4])
