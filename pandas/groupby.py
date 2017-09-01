import numpy as np 
import pandas as pd

data = {'Company':'GOOG GOOG MSFT MSFT FB FB'.split(),
		'Person':'Sam Charlie Amy Vanessa Carl Sarah'.split(),
		'Sales':[200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)

# vamos a ver como usar groupby que son objetos con ciertos
# metodos que nos muestran los datos con procesos, que sabe
# identificar cuando un indice se repite es como lo mismo

# con esto creamos un objeto groupby

groupby = df.groupby('Company')

# con este metodo sacamos el promedio de sales

groupby.mean()

# solo da el resultado de sales porque se da cuenta que son
# strings la otra columna y no puede sacar promedio de strings

# tenemos estos metodos y mas

groupby.sum() 	# suma de todos
groupby.std()	# desviacion standard
groupby.count()	# cuenta las repeticiones del indice
groupby.max()	# el valor mas alto
groupby.min()	# el valor mas bajo

# si solo queremos con un que no muestre una fila usa .loc[]

groupby.sum().loc['FB']
# Sales    593
# Name: FB, dtype: int64

# el metodo mas util para un gruupby es .describe() que nos da
# mucha informacion del datafram

groupby.describe().loc['FB']
#             Sales
# count    2.000000
# mean   296.500000
# std     75.660426
# min    243.000000
# 25%    269.750000
# 50%    296.500000
# 75%    323.250000
# max    350.000000