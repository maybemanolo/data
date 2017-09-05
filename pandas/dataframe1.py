# un dataframe es lo pincipal de pandas

import numpy as np
import pandas as pd
from numpy.random import randn

# cuando seguimos a alguien en un tutorial o algo y queremos
# que hasta los valores random sean igual usamos .seed()

np.random.seed(101)

# para crear un dataframe usamos

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509


# le estamos estamos haciendo que genere una forma de 5x4
# y le decimos tambien que use la primera lista como index (Y)
# y la segunda como columnas (X)

# las columnas realmente son series dentro de un dataframe
# para acceder a ellas es como una lista/diccionario

df['W']
# A    2.706850
# B    0.651118
# C   -2.018168
# D    0.188695
# E    0.190794
# Name: W, dtype: float64

# para acceder a varias columnas usamos una lista

df[['W','Z']]
#           W         Z
# A  2.706850  0.503826
# B  0.651118  0.605965
# C -2.018168 -0.589001
# D  0.188695  0.955057
# E  0.190794  0.683509

# cuando queremos crear una nueva columna dentro para un 
# dataframe hacemos como accedieramos a una pero le asignamos
# una lista

df['new'] = [1,2,3,4,5]
#           W         X         Y         Z  new
# A  2.706850  0.628133  0.907969  0.503826    1
# B  0.651118 -0.319318 -0.848077  0.605965    2
# C -2.018168  0.740122  0.528813 -0.589001    3
# D  0.188695 -0.758872 -0.933237  0.955057    4
# E  0.190794  1.978757  2.605967  0.683509    5

# para borrar una columna usamos el metodo df.drop(), al cual 
# le tenemos que pasar 2 parametros, la columna/index y el
# axis (X o Y) index = 0 , columna = 1

df.drop('new',axis=1)
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509

# acordarse que esto no afecta a la variable df sino se tiene
# que guardar el output en otra variable

new_df = df.drop('new',axis=1)

# para encontrar una fila (X o indice) usamos este metodo

df.loc['D']
# W      0.188695
# X     -0.758872
# Y     -0.933237
# Z      0.955057
# new    4.000000
# Name: D, dtype: float64

# multiples filas

df.loc[['D','C']]
#           W         X         Y         Z  new
# D  0.188695 -0.758872 -0.933237  0.955057    4
# C -2.018168  0.740122  0.528813 -0.589001    3

# aqui notamos que tambien las filas son series solo que
# necesitamos otros metodos para accederlos

# el mismo metodo que usamos para filas, lo usamos para 
# buscar ciertas filas y columnas a la vez

df.loc[['A','B'],['X','Y']]
#           X         Y
# A  0.628133  0.907969
# B -0.319318 -0.848077