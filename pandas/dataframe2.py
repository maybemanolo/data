import numpy as np 
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

# una de las cosas mas importantes en pandas son las
# selecciones condicionales, donde le ponemos una condicion
# adentro de brackets y nos devuelve un dataframe lleno
# de valores booleanos, lo que pasa es que compara cada celda
# y devuelve el valor en cada celda en todo el dataframe

bool_df = df > 0
#        W      X      Y      Z
# A   True   True   True   True
# B   True  False  False   True
# C  False   True   True  False
# D   True  False  False   True
# E   True   True   True   True

# una vez que tenemos el dataframe donde tenemos solo valores
# booleanos lo usamos como index en el dataframe, y solo nos
# va devolver los valores donde haya true y devolvera NaN
# donde sea false

df[bool_df]
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118       NaN       NaN  0.605965
# C       NaN  0.740122  0.528813       NaN
# D  0.188695       NaN       NaN  0.955057
# E  0.190794  1.978757  2.605967  0.683509

# esto se puede hacer en un paso asi

df[df>0]

# cuando usamos esta clase de metodos nos va devolver campos
# con el valor NaN donde habia un valor False, pero si en
# en lugar paso un serie de valores booleanos como la 
# comparacion de una columna, conoseguimos los filas donde
# los valores eran True

df['W']>0
# A     True
# B     True
# C    False
# D     True
# E     True
# Name: W, dtype: bool

df[df['W']>0]
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509

# claro que podemos acceder  las columnas de las maneras
# como una lista arr[x] y tambien para multples usamos
# df[x,y]

df[df['W']>0][['Y','X']]
#          Y         X
# A  0.907969  0.628133
# B -0.848077 -0.319318
# D -0.933237 -0.758872
# E  2.605967  1.978757

# cuando vamos a usar operadores logicos como and no 
# podemos usar la palabra normal porque es sobre un dataframe
# tenemos que usar el simbolo &

# la siguiente condicional checa los valores de columna W e
# Y , que devuelva la fila donde W > 0 e Y > 1

df[(df['W']>0) & (df['Y']>1)]
#           W         X         Y         Z
# E  0.190794  1.978757  2.605967  0.683509

# y para usar el operador or usamos |

df[(df['W']>0) | (df['Y']>1)]
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509

# para eliminar el index que personalizamos y usar el default
# usamos el metodo df.reset_index() que no actua sobre el df
# sino se tiene que asignar de nuevo o usar el parametro
# in_place=True

df.reset_index()

# si queremos cambiar una columna para que sea el index (Y)
# usamos este metodo

new_index = 'CA NY WY OR CO'.split()
df['States'] = new_index
df.set_index('States')

