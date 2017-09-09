import matplotlib.pyplot as plt
import seaborn as sns
flights = sns.load_dataset('flights')

# para crear un dataframe en forma de matrix usamos el
# metodo pivot_table()

fp = flights.pivot_table(index='month',columns='year',values='passengers')

# podemos usar el heatmap para que nos muestre la info
# de manera concentrada, con heatmap donde cmap define
# los colores

sns.heatmap(fp,cmap='magma',linecolor='white',linewidth=1)
plt.show()

# se puede crear un mapa cluster de la siguiente manera,
# que ordena la informacion de manera que haga que se 
# parezca la que tiene a los lados

sns.clustermap(fp)
plt.show()