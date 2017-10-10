# un recomender system es aquel que como implica la palabra te
# recomienda, cosas como peliculas en netflix o articulos en 
# amazon

# tenemos dos tipos de recosys tenemos content base y collaborative
# filtering, los de contet base se basa en los atributos de algo
# para recomendar cosas, mientras que collaborative se basa en
# demas usarios que tambien hacen lo mismo que tu

# vamos a crear un recomender system content base

import pandas as pd
import numpy as np

# creamos nuestro dataset

column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('u.data', sep='\t', names=column_names)

movie_titles = pd.read_csv("Movie_Id_Titles.csv")
df = pd.merge(df,movie_titles,on='item_id')

# vamos a hacer una visualizaciones

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.rcParams["patch.force_edgecolor"] = True

# esto nos va mostrar el rating de cada pelicula de mejor a peor

df.groupby('title')['rating'].mean().sort_values(ascending=False)

# esto nos muestran las peliculas con mas calificaciones

df.groupby('title')['rating'].count().sort_values(ascending=False)

# creamos otro dataframe con esta nueva info

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())

# ahora graficamos un histograma con la cantidad de rating que
# tiene cada pelicula

ratings['num of ratings'].hist(bins=70)
plt.show()

# ahora hacemos un histograma para ver los rating de las peliculas

ratings['rating'].hist(bins=70)
plt.show()

# ahora comparamos las dos graficamos a ver si vemos una relacion

sns.jointplot(x='rating',y='num of ratings',data=ratings,alpha=0.1)
plt.show()

# ahora construimos el modelo

# primero creamos un pivot table 

moviemat = df.pivot_table(index='user_id',columns='title',values='rating')

# luego vamos a checar nuestro peliculas con mas ratings

ratings.sort_values('num of ratings',ascending=False)

# elegimos 1 pelicula

starwars_user_ratings = moviemat['Star Wars (1977)']

# buscamos la relacion entre todas las peliculas con Star Wars

similar_to_starwars = moviemat.corrwith(starwars_user_ratings)

# ahora creamos un dataset a partir de la correlacion

corr_starwars = pd.DataFrame(similar_to_starwars,columns=['Correlation'])
corr_starwars.dropna(inplace=True)

# de los problemas que vamos a tener es que hay algunas peliculas
# es que tienen una correlacion de 1 que vemos asi

corr_starwars.sort_values('Correlation',ascending=False)

# esto pasa por usuarios que le dan la misma calificaion a peliculas
# con solo un rating que Star Wars, podemos filtrar a los resultados
# a partir de cierto numero

corr_starwars = corr_starwars.join(ratings['num of ratings'])

# quitamos todas donde no hayan al menos 100 ratings

corr_starwars = corr_starwars[corr_starwars['num of ratings'] > 100].sort_values('Correlation',ascending=False)