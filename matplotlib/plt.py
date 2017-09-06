# matplotlib es una libreria la cual se encarga de visualizar
# datos, graficando en 2d o 3d, casi siempre se usa solo
# pyplot

import matplotlib.pyplot as plt

# para correr matplotlib en la jupyter notebook usamos esta
# linea sin comentar

# %matplotlib inline

# generamos dos arrays para estarlos graficarlos

import numpy as np 
X = np.linspace(0,5,11)
Y = X ** 2

# para grafica usamos la funcion plt.plot(), donde le pasamos
# los valores X y Y de la grafica

plt.plot(X,Y)

# asi mostramos la grafica

plt.show()

# podemos agregar un titulo para los valores X y Y, y un
# titulo a la grafica

plt.plot(X,Y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Titulo')

plt.show()

# podemos crear subplot que permite crear mas de un grafica

plt.subplot(1,2,1)
plt.plot(X,Y,'r')

plt.subplot(1,2,2)
plt.plot(X,Y,'b')

plt.show()

# existe otra manera de graficar de manera OO

fig = plt.figure()

# con esto modelamos el canvas en que vamos a graficar

axes = fig.add_axes([0.1,0.1,0.8,0.8])

# que tan lejos de la izquierda, que tan lejos de abajo,
# que tan alto y que tan grueso

# esta son las opciones

axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Titulo')

# para poner los valores en el canvas

axes.plot(X,Y)

plt.show()

# tambien con este metodo podemos usar subplots(), y le
# tenemos que especificar el numero de columnas y filas
# en grafica

fig, axes = plt.subplots(nrows=1,ncols=2)

# para que no se sature informacion usamos

plt.tight_layout()

# esto nos devuelve un array que esta lleno de elementos
# que son graficas osea que podemos iterar

for current in axes:
	current.plot(x,y)
plt.show()

# o accesar a los elementos

axes[0].plot(x,y)
plt.show()

# al momento de hacer una figura podemos indicar el numero de
# columnas y filas, tambien el tamano de la figura con una
# tupla (width y length)

fig,axes = pl.subplots(nrows=2,ncols=1,figsize=(8,2))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()
plt.show()

# para salvar como foto usamos, dpi es cuanto detalle

fig.savefig('grafica.png',dpi=200)

# podemos usar legends para referirnos usando un parametros
# mas en .plot() para poner un label, ponemos un .legend()
# al final para que muestre las labels, y le ponemos 0 para
# que use el mejor lugar de la grafica

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label='X Cuadrada')
ax.plot(x,x**3,label='X Cubica')
ax.legend(loc=0)

# podemos personalizar cosas de cada linea como su estilo
# color y mas cosas

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y, color='orange')
plt.show()

# los colores que podemos usar en una linea pueden ser
# hexadecimales, o strings como

# b: blue
# g: green
# r: red
# c: cyan
# m: magenta
# y: yellow
# k: black
# w: white

# podemos alterar que tan grueso es la linea, siendo 1 el
# normal y 2 el doble

ax.plot(x,y, linewidth=2) #lw
plt.show()

# podemos tambiar cambiar que tan translucida es una linea

ax.plot(x,y, alpha=0.5)
plt.show()

# podemos cambiar el estilo de linea asi como

ax.plot(x,y, linestyle='--') #ls
plt.show()

# tenemos opciones como
# : ..........
# -. _._._._._
# -- ---------
# - __________

# podemos utilizar markers para poner puntos cruciales pero
# generalmente usamos solo un punto

ax.plot(x,y, marker='o', markersize=5, markerfacecolor='yellow')
plt.show()

# para cambiar el inicio de X y Y en la grafica usamos

ax.set_xlin([0,1])
ax.set_ylin([0,2])
plt.show()