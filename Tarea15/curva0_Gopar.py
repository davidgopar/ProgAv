'''
David Gopar Morales
Fractal de Hilbert en python con matplotlib
Programación Avanzada
'''

# Version desde caso n = 0
from matplotlib import pyplot as plt


def A(n, x, y):
	if n == 0: #Dibuja linea a la izquierda
		x1 = x - 1
		y1 = y
		plt.plot([x, x1], [y, y1], color='red')
		return x1, y1
	if n==1:
		x, y = A(0,x,y)
		x, y = B(0,x,y)
		x, y = C(0,x,y)
		return x, y
	else:
		x , y = B(n-1, x ,y)
		x , y = A(0,x,y)
		x , y = A(n-1,x , y)
		x , y = B(0,x, y)
		x , y = A(n-1, x , y)
		x , y = C(0,x,y)
		x , y = D(n-1, x, y)

		return x , y

def B(n, x, y):
	if n == 0: # Dibuja linea abajo
		x1 = x 
		y1 = y -1
		plt.plot([x, x1], [y, y1], color='blue')
		return x1, y1
	if n == 1:
		x , y = B(0,x,y)
		x , y = A(0,x,y)
		x , y = D(0,x,y)
		return x , y
	else:
		x , y = A(n-1, x , y)
		x , y = B(0,x, y)
		x , y = B(n-1, x , y)
		x , y = A(0,x, y)
		x , y = B(n-1, x , y)
		x , y = D(0,x, y)
		x , y = C(n-1, x , y)
		return x, y

def C(n, x, y):
	if n == 0: # Dibuja linea derecha
		x1 = x + 1
		y1 = y
		plt.plot([x, x1], [y, y1], color='navy')
		return x1, y1

	if n == 1:
		x , y = C(0,x, y)
		x , y = D(0,x, y)
		x , y = A(0,x, y)
		return x , y
	else:
		x , y = D(n-1, x , y)
		x , y = C(0,x,y)
		x , y = C(n-1, x, y)
		x , y = D(0,x,y)
		x , y = C(n-1, x , y)
		x , y = A(0,x,y)
		x , y = B(n-1, x, y)
		return x , y
def D(n, x, y):
	if n == 0: # Dibuja linea arriba
		x1 = x 
		y1 = y +1
		plt.plot([x, x1], [y, y1], color='purple')
		return x1, y1
	if n == 1:
		x , y = D(0,x , y)
		x , y = C(0,x , y)
		x , y = B(0,x , y )
		return x , y
	else:
		x , y = C(n-1, x, y)
		x , y = D(0,x , y)
		x , y = D(n-1, x, y)
		x , y = C(0,x , y)
		x , y = D(n-1, x , y)
		x , y = B(0,x, y)
		x , y = A(n-1, x, y)
		return x , y

x,y = A(5,0,0)
plt.axis('equal') # same lengths in x and y direction
plt.axis('off')
plt.show()
