# en pandas nos permite usar unos nuevos tipos de datos como
# series, que es como un numpy array, de hecho esta escrito
# sobre numpy

import numpy as np
import pandas as pd

# vamos a crear unas variables

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
dic = {'a':10 ,'b':20 ,'c':30}

# ahora vamos a crear un series, sirve igual si usamos un
# numpy array en lugar de una lista

serie_list = pd.Series(data=my_data)
# 0 	10
# 1		20
# 2		30
# dtype: int64

# esto se parece masomenos aun array tenemos un valor y su
# index, pero podemos cambiar el index pasando otra lista
# con la misma cantidad de elementos

serie_index = pd.Series(data=my_data, index=labels)
# a 	10
# b		20
# c		30
# dtype: int64

# cuando le pasamos un diccionario asume automatica el index
# y data

serie_dic = pd.Series(dic)

# para indexing en un panda serie se usa igual que un
# diccionario o una lista, depende el idex que elegimos

serie_index['a']
serie_dic['b']
serie_list[2]

# cuando hacemos aritmetica con series va checar en los
# indices cuales coinciden y va a realizar la operacion
# pero cuando no la encuetra pone NaN en su lugar

ser_1 = pd.Series(data=[1,2,3,4],index=['USA','GER','USSR','JPN'])
ser_2 = pd.Series(data=[1,2,5,4],index=['USA','GER','ITA','JPN'])

print(ser_1 + ser_2)