# natural lenguaje processing es una tecnica para que un programa
# pueda entender un texto un ejemplo simple es hacer una lista de 
# las posible palabras dentro de un str y simplemente se hace un
# lista de las que estan y las que no

# se puede encontrar la similaridad matematicamente

# vamos a hacer un algoritmo que detecte si un mensaje es spam o no

import nltk

# para descargar un dataset, podemos tener una sesion interactiva
# con nltk.download_shell()

# o usar este comando y especificar el dataset
# nltk.download('stopwords')

# ahora vamos a importar nuestro dataset

messages = [line.rstrip() for line in open('smsspamcollection/SMSSpamCollection')]

# imprimimos los primeros 10

for mess_no,message in enumerate(messages[:10]):
	print(mess_no,message)
	print('\n')

# ahora creamos un dataframe

import pandas as pd
messages = pd.read_csv('smsspamcollection/SMSSpamCollection',sep='\t',names=['label','message'])

# hacemos una pequeña exploracion de datos

messages.describe()
messages.groupby('label').describe()

# creamos una nueva columna para intentar ver patrones con el numero
# de caracteres en spam y ham

messages['len'] = messages['message'].apply(len)

# hacemos visualizaciones

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.rcParams["patch.force_edgecolor"] = True

messages['len'].plot.hist(bins=100)
plt.show()

# buscamos el mensaje mas largo

messages['len'].describe()
messages[messages['len'] == 910]['message'].iloc[0]

# ahora graficamos una con solo ham y otra con spam para comparar
# graficas

messages.hist(column='len',by='label',bins=60,figsize=(12,4))
plt.show()

# el problema que tenemos aqui es que tenemos un dataset de strings
# no de valores que es lo que necesitamos para usar los algoritmos
# de clasificaion que ya tenemos

# bag of words

# vamos a convertir los strings en vectores para poder usarlos,
# queremos eliminar palabras normales que estan en stopwords

# primero limpiamos nuestro string

import string

mess = 'Sample String .!!@#$%^&*('
nopunc = [char for char in mess if char not in string.punctuation]

from nltk.corpus import stopwords
stopwords.words('english')

nopunc = ''.join(nopunc)

clean_mess = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

# ahora definimos nuestra funcion

def text_process(mess):
	nopunc = [c for c in mess if c not in string.punctuation]
	nopunc = ''.join(nopunc)
	return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

# aplicamos el metodo

messages['message'].apply(text_process)

# ahora vamos hacer una dataframe donde vienen todas las palabras
# y cuantas veces se repite en cada mensaje

# un sparse matrix es un matri con muchos ceros lo cual vamos a
# generar

# vamos a construir el matrix

from sklearn.feature_extraction.text import CountVectorizer

bow_transformer = CountVectorizer(analyzer=text_process).fit(messages['message'])

# veremos cuantas palabras tenemos

print(len(bow_transformer.vocabulary_))

# elegiremos un mensajes y checaremos su bag of words

mess4 = messages['message'][3]
bow4 = bow_transformer.transform([mess4])

# ahora imprimimos el valor de bow4

print(bow4)

# esto me muestra que palabra (con su index) y cuantas veces se 
# repite en la oracion que le pasamos

# vemos a que palabra se refiere de la siguiente manera

bow_transformer.get_feature_names()[9554]

# ahora transformamos todo el dataset

messages_bow = bow_transformer.transform(messages['message'])

# para checar cuantos valores no son ceros podemos usar

messages_bow.nnz

# para saber sparcity usamos una formula, el resultado de esto
# es el porcentaje de valores non zeros

sparsity = (100.0 * messages_bow.nnz / (messages_bow.shape[0] * messages_bow.shape[1]))
print('sparcity:',sparsity)

# ahora vamos a conseguir tfidf con scikit learn, el cual nos deci
# que tan importante es una palabra en una dada

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer().fit(messages_bow)
tfidf4 = tfidf_transformer.transform(bow4)

print(tfidf4)

# ahora vamos a convertur todo a tfidf

messages_tfidf = tfidf_transformer.transform(messages_bow)

# vamos a hacer un pipe line

from sklearn.naive_bayes import MultinomialNB

spam_detect_model = MultinomialNB().fit(messages_tfidf,messages['label'])

# ahora podemos predecir

spam_detect_model.predict(tfidf4)[0]

# pero necesitamos usar train test split

from sklearn.model_selection import train_test_split

msg_train,msg_test,label_train,label_test = train_test_split(messages['message'],messages['label'],test_size=0.3)

# y todo esto lo podemos hacer con esto

from sklearn.pipeline import Pipeline

pipeline = Pipeline([
		('bow',CountVectorizer(analyzer=text_process)),
		('tfidf',TfidfTransformer()),
		('classifier',MultinomialNB())
	])

pipeline.fit(msg_train,label_train)

# ahora predecimos

predictions = pipeline.predict(msg_test)

from sklearn.metrics import classification_report

print(classification_report(label_test,predictions))