# tenemos mucahs maneras de personalizar las graficas que
# generamos con seaborn

import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

sns.countplot(x='sex',data=tips)

# tenemos todo un metodo para cambiar estilos

sns.set_style('white') # fondo blaco
sns.set_style('ticks') # conseguir ticks
sns.set_style('darkgrid') # lineas
sns.set_style('whitegrid')# lineas

# para quitar las lineas de arriba y derecha usamos

sns.despine()

# para cambiar tamanos usamos

sns.set_context('poster') # se puede cambiar context

plt.show()

# para ver que paletas de colores podemos usar en las 
# graficas estan en la pagina:
# https://matplotlib.org/examples/color/colormaps_reference.html