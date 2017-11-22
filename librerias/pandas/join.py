import numpy as np
import panda as pd
from numpy.random import randn

df1 = pd.DataFrame({'A':'A0 A1'.split(),
					'B':'B0 B1'.split()},
					index=[0,1])

df2 = pd.DataFrame({'A':'A2 A3'.split(),
					'B':'B2 B3'.split()},
					index=[2,3])

df3 = pd.DataFrame({'A':'A4 A5'.split(),
					'B':'B4 B5'.split()},
					index=[4,5])

# lo que vamos es hacer es juntar dos dataframes de diferentes
# maneras

# la primer es concatenacion, ten en cuenta que ambos
# dataframes necesitan tener las mismas dimensiones

pd.concat([df1,df2,df3])
# 0  A0  B0
# 1  A1  B1
# 2  A2  B2
# 3  A3  B3
# 4  A4  B4
# 5  A5  B5

# podemos unirlos por medio de columnas cambias el axis a 1

pd.concat([df1,df2,df3], axis=1)
#      A    B    A    B    A    B
# 0   A0   B0  NaN  NaN  NaN  NaN
# 1   A1   B1  NaN  NaN  NaN  NaN
# 2  NaN  NaN   A2   B2  NaN  NaN
# 3  NaN  NaN   A3   B3  NaN  NaN
# 4  NaN  NaN  NaN  NaN   A4   B4
# 5  NaN  NaN  NaN  NaN   A5   B5

left = pd.DataFrame({'key':'K0 K1 K2'.split(),
					'A':'A0 A1 A2'.split(),
					'B':'B0 B1 B2'.split()})

right = pd.DataFrame({'key':'K0 K1 K2'.split(),
					'C':'C0 C1 C2'.split(),
					'D':'D0 D1 D2'.split()})

# en este caso tenemos una columna en comun en ambos dataframes,
# usamos merge que es igual que en SQL, le decimos que 
# dataframes, con que metodo (inner) y sobre cual columna

pd.merge(left,right,how='inner',on='key')
#     A   B key   C   D
# 0  A0  B0  K0  C0  D0
# 1  A1  B1  K1  C1  D1
# 2  A2  B2  K2  C2  D2