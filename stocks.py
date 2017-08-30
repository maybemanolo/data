# en este ejemplo vamos analizar acciones de la ampresa Apple y
# vamos a predecir sus futuros valores

# vamos usar librerias para leer archivos .csv (csv) numpy
# para calculos sklearn para modelos y matplotlib para
# graficar

import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR

plt.switch_backend('MacOSX')

# creamos variables para guardar fechas con sus precios

dates = []
prices = []

# delcaramos una funcion para llenar esa lista de valores

def get_data(filename):
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader)
		for row in csvFileReader:
			dates.append(int(row[0].split('-')[0]))
			prices.append(float(row[1]))
	return

# ahora creamos la funcion con la que vamos analizar

def predict_price(dates, prices, x):

	# la funcion np.reshape() es cambiar las dimensiones de un
	# array, aqui le indicamos a cual (dates), y le paso las 
	# dimesiones como una tupla la cual del len(dates) y 1 lo
	# que siginifica que es de una dimension

	dates = np.reshape(dates, (len(dates), 1))

	# ahora no solo vamos a importar un modelo para entrenar 
	# sino vamos a crear uno, todos seran un tipo de Support
	# Vector Machine, esto significa que tenemos nuestros datos
	# distribuidos en un grafica y se crea una linea entre 
	# lo datos que son diferentes, pero como en este caso 
	# queremos hacer prediccion usamos Support Vector Regression
	# que analiza los datos (distancia) e intenta predecir
	# donde estara el proximo

	# estos son nuestros modelos el paramtro kernal significa que
	# tipo de SVR() va ser, C que es el error, cuando hacemos una
	# SVR aveces no se puede usar una linea que separe a todos y 
	# que tambien este en el centro de la mayoria, C define a
	# partir de cuando es error, degree es el angulo y gamma dice
	# cuanto es lejos 

	svr_lin = SVR(kernel='linear', C=1e3)
	svr_poly = SVR(kernel='poly', C=1e3, degree=2)
	svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)

	# entrenamos modelos

	svr_rbf.fit(dates, prices)
	svr_lin.fit(dates, prices)
	svr_poly.fit(dates, prices)

	# graficamos con matplotlib

	plt.scatter(dates, prices, color= 'black', label= 'Data') # plotting the initial datapoints 
	
	plt.plot(dates, svr_rbf.predict(dates), color= 'red', label= 'RBF model') # plotting the line made by the RBF kernel
	plt.plot(dates,svr_lin.predict(dates), color= 'green', label= 'Linear model') # plotting the line made by linear kernel
	plt.plot(dates,svr_poly.predict(dates), color= 'blue', label= 'Polynomial model') # plotting the line made by polynomial kernel
	
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title('Support Vector Regression')

	plt.legend()
	plt.show()

	# retornamos las predicciones

	return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

get_data('aapl.csv')

predicted_price = predict_price(dates, prices, 29) 
print(predicted_price) 