import numpy as np
import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],
				   'col2':[444,555,666,444],
				   'col3':'abc def ghi xyz'.split()})

# para encontrar que valores son unicos dentro de una columna
# de un dataframe, nos devuelve un array de numpy

df['col1'].unique()
# array([1, 2, 3, 4])

# para conseguir el numero de valores unicos

df['col1'].nunique()
# 4

# este metodo nos devuelve una serie que nos dice que numeros
# hay y cuantas veces se repiten

df['col2'].value_counts()
# 444    2
# 555    1
# 666    1
# Name: col2, dtype: int64

# para aplicar una funcion (lambda) o una keyword o todos los 3
# valores de una serie o dataframe 

df.apply(lambda x: x*2)
#    col1  col2    col3
# 0     2   888  abcabc
# 1     4  1110  defdef
# 2     6  1332  ghighi
# 3     8   888  xyzxyz

df['col3'].apply(len)
# 0    3
# 1    3
# 2    3
# 3    3
# Name: col3, dtype: int64

# dataframes tienes propiedades que nos dan informacion de si
# mismo, como

df.columns()	# nombre de columnas
df.index()		# valores de index

# podemos ordenar una dataframe por medio de la columna que
# especifiquemos

df.sort_values('col2')
#    col1  col2 col3
# 0     1   444  abc
# 3     4   444  xyz
# 1     2   555  def
# 2     3   666  ghi

# tenemos un metodo para saber cuales valores dentro de un
# dataframe son null

df.isnull()
#     col1   col2   col3
# 0  False  False  False
# 1  False  False  False
# 2  False  False  False
# 3  False  False  False

