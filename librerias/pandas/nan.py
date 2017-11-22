import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
#      A    B  C
# 0  1.0  5.0  1
# 1  2.0  NaN  2
# 2  NaN  NaN  3

# cuando tenemos valores entre nuestro dataframe que son not a
# number o NaN tenemos que deshacernos de ellos, no de las 
# filas o columnas siempre pero si de los espacios

# tenemos metodos como df.dropna() que no elimina todas las
# columnas o filas que tengan NaN, le definimos con el
# parametro axis si sera columna o fila

# elimina filas, si no le pasamos el parametro este es default

df.dropna(axis=0)
#      A    B  C
# 0  1.0  5.0  1

# elimina columnas

df.dropna(axis=1)
#    C
# 0  1
# 1  2
# 2  3

# tenemos otro parametro que nos da la opcion de tener filas o
# columnas con una cantidad de valores nan, el parametro thresh
# nos dice por lo menos cuanto no nan valores tiene que haber
# en una fila o columna

df.dropna(thresh=2)
#      A    B  C
# 0  1.0  5.0  1
# 1  2.0  NaN  2

# tenemos metodo que nos permite remplazar todos los valores nan
# por otro con una funcion

df.fillna(value="remplazo")
#           A         B  C
# 0         1         5  1
# 1         2  remplazo  2
# 2  remplazo  remplazo  3

# cuando tenemos un valor nan es bueno aveces llenar ese valor 
# con el promedio asi

df['A'].fillna(value=df['A'].mean())