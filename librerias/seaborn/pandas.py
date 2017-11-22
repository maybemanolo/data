# tambien podemos visualizar cosas como en seaborn o 
# matplotlib pero directamente en pandas

import numpy as np
import seaborn as sns
import pandas as pd

df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))

# podemos crear un histogram de un dataframe asi

df['A'].hist(bins=30)

# todos los metodos para graficar e encuentran dentro de
# el metodo plot

df['A'].plot.hist()				# histograma
df.plot.are()					# area
df.plot.bar()					# barras
df.plot.line(x=df.index,y='B')	# linea
df.plot.scatter(x='A',y='B')	# scatter
df.plot.bow()					# boxplot