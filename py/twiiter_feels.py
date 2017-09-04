# ahora vamos a crear un programa que analize tweets y va saber
# si es tristo o feliz (sus sentimientos pues)

# primero tenemos que conectar el programa con el API de twitter
# usando la libreria twitter

import tweepy

consumer_key = "Uc1K3BY2tCLPY5LLgEBjGeLIp"
consumer_secret = "ztoS337lQSUxeaMR9RqNV4ER1wtHNHCatCD3mNXvoopNsKOU6g"

acces_token = "433165406-ZdZvo5VdIWpVMLbfyM40Sh39sInwI178328CZM7U"
acces_token_secret = "ybigiHk4F5qA4kDtgmnfwUYA4bmffsvzGNULYfjGmYKuw"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acces_token, acces_token_secret)

api = tweepy.API(auth)

# ahora tenemos que recolectar data (tweets en este caso) entonces con
# la misma api podemos buscar tweets que contengan una palabra

public_tweets = api.search("Trump")

# textblob es un libreria que vamos a necesitar para saber el valor
# sentimental de cada tweet, es una libreria para NLP pero ya tiene
# incluida una funcion para clasificar el sentimiento

from textblob import TextBlob

# ahora vamos a imprimir el atributo .text de cada tweet, lo que el
# tweet pero en string, deespues vamos hacer una analisis con creando
# un objeto textblob y usando su propiedad sentiment para saber si
# es positivo o negativo (polarity) y tambien si es un hecho u opinion
# (subjectivity)

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

# reto

csv = open("twiiter_feels.csv", "w+")

for tweet in public_tweets:

	analisis = TextBlob(tweet.text)

	if analisis.sentiment.polarity > 0:
		analisis = " Good"
	elif analisis.sentiment.polarity <= 0:
		analisis = " Bad"
	else:
		analisis = " No c"

	csv.write(tweet.text + str(analisis) + '\n')

csv.close()