# vamos hacer un sistema de recomendaciones para peliculas
# usamos librerias como numpy y scipy para hacer los
# calculos de nuestro programa y lightfm para el
# recomedation system

import scipy
import numpy as np
from lightfm import LightFM

# ahora vamos a importar el dataset sobre el que vamos a
# entrenar el modelo

from lightfm.datasets import fetch_movielens

# vamos a recolectar del dataset en una variable, que solo
# tengan minimo 4.0 de calificacion

data = fetch_movielens(min_rating=4.0)

# cuando usamos el metodo fetch_movies nos trae un 
# un diccionario con los labels train y test

print(repr(data['train']))
print(repr(data['test']))

# ahora vamos a crear nuestro modelo que vamos a entrenar, 
# le tenemos que pasar un parametro loss, que es una funcion
# mide la diferencia la predccion del modelo y nuestro 
# resultado deseado, sirve para que nuestar prediccion cada 
# vez sea mas precisa, vamos usar modo warp (Weighted 
# Approximate-Rank Pairwise) que usa el algoritmo gradient 
# descent

model = LightFM(loss='warp')

# ahora vamos entrenar nuestro modelo con los parametros, el
# primer es dataset con el que se va entrenar, luego epochs
# que es la veces que va analizar el dataset de ida y regreso
# y como ultmo num_threads dice cuantos threads se van a
# usar

model.fit(data['train'], epochs=30, num_threads=2)

# sigues una funcion que va hacer la recomendacion en si

def sample_recommedation(model, data, user_ids):

	# vamos a crear variables con la figura del dataset, para
	# saber cuantas usuarios y peliculas hay

	n_users, n_items = data['train'].shape

	# vamos hace un for loop en cada user para ver que ya les
	# gusto a cada usario

	for user_id in user_ids:

		# el dataset considera 5 estrellas positivo mietras de
		# 4 para abajo es negativo

		# con esta funcion sabemos que cosas ya le han gustado
		# al user 

		known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

		# hacemos las prediciones de las peliculas que quiza
		# van a gustar, pasandolo X que es el user_id y Y que
		# es el rango de la calificacion

		scores = model.predict(user_id, np.arange(n_items))

		# esto va elegir las mejores peliculas 

		top_items = data['item_labels'][np.argsort(-scores)]

		# ahora solo imprimimos resultados

		print("User ID: " + str(user_id))
		print("Positives: ")

		for x in known_positives[:3]:
			print("		" + str(x))

		print("Recomended: ")

		for x in top_items[:3]:
			print("		" + str(x))

sample_recommedation(model, data, [3,25,450])