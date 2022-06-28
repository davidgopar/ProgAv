'''
David Gopar Morales
Fractal de Hilbert en python con matplotlib
Programación Avanzada
'''

from matplotlib import pyplot as plt

# Nota: las funciones dibuja_%%%%(x, y)
# 		se pueden sustituir por una solafunción
# 		a la cual se le pase otro parámetro (a,b),
# 		con a,b \in {0,1,-1},
# 		los cuales indican para donde moverse
# 		pero es más ilustrativo ver como se decide 
# 		moverse.

def dibuja_izquierda(x0,y0):
	x1 = x0 - 1
	y1 = y0
	plt.plot([x0, x1], [y0, y1], color='red')
	return x1, y1

def dibuja_derecha(x0,y0):
	x1 = x0 + 1
	y1 = y0
	plt.plot([x0, x1], [y0, y1], color='navy')
	return x1, y1

def dibuja_abajo(x0,y0):
	x1 = x0 
	y1 = y0 -1
	plt.plot([x0, x1], [y0, y1], color='blue')
	return x1, y1


def dibuja_arriba(x0,y0):
	x1 = x0 
	y1 = y0 +1
	plt.plot([x0, x1], [y0, y1], color='purple')
	return x1, y1

def A(n, x, y):
	if n==1:
		x, y = dibuja_izquierda(x,y)
		x, y = dibuja_abajo(x,y)
		x, y = dibuja_derecha(x,y)
		return x, y
	else:
		x , y = B(n-1, x ,y)
		x , y = dibuja_izquierda(x,y)
		x , y = A(n-1,x , y)
		x , y = dibuja_abajo (x, y)
		x , y = A(n-1, x , y)
		x , y = dibuja_derecha(x,y)
		x , y = D(n-1, x, y)

		return x , y

def B(n, x, y):
	if n == 1:
		x , y = dibuja_abajo(x,y)
		x , y = dibuja_izquierda(x,y)
		x , y = dibuja_arriba(x,y)
		return x , y
	else:
		x , y = A(n-1, x , y)
		x , y = dibuja_abajo(x, y)
		x , y = B(n-1, x , y)
		x , y = dibuja_izquierda(x, y)
		x , y = B(n-1, x , y)
		x , y = dibuja_arriba(x, y)
		x , y = C(n-1, x , y)
		return x, y

def C(n, x, y):
	if n == 1:
		x , y = dibuja_derecha(x, y)
		x , y = dibuja_arriba(x, y)
		x , y = dibuja_izquierda(x, y)
		return x , y
	else:
		x , y = D(n-1, x , y)
		x , y = dibuja_derecha(x,y)
		x , y = C(n-1, x, y)
		x , y = dibuja_arriba(x,y)
		x , y = C(n-1, x , y)
		x , y = dibuja_izquierda(x,y)
		x , y = B(n-1, x, y)
		return x , y
def D(n, x, y):
	if n == 1:
		x , y = dibuja_arriba(x , y)
		x , y = dibuja_derecha(x , y)
		x , y = dibuja_abajo(x , y )
		return x , y
	else:
		x , y = C(n-1, x, y)
		x , y = dibuja_arriba(x , y)
		x , y = D(n-1, x, y)
		x , y = dibuja_derecha(x , y)
		x , y = D(n-1, x , y)
		x , y = dibuja_abajo(x, y)
		x , y = A(n-1, x, y)
		return x , y

x,y = A(5,0,0)
plt.axis('equal') # same lengths in x and y direction
plt.show()
