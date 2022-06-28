#David Gopar Morales
#Programa para verificar si un diccionario es un grupo
#Junto con otras operaciones posibles a efectuar

class Group:
	def __init__(self, tabla):
		self.tabla = tabla
		self.e = Obtener_elementos(tabla)
		self.grupo = Ver_grupo(tabla)
		if self.grupo == 'Si':
			self.neutro = Ver_neutro(tabla)[0]
			self.inversos = Ver_inversos(tabla)[0] 

class element:
	def __init__(self, a, Group):
		if a in Group.e:
			self.elemento = a
			self.grupo = Group

	def __str__(self):
		return self.elemento

	def __add__(self, other):
		x = self.grupo.tabla[(self.elemento, other.elemento)]
		return element(x, self.grupo)

	def __sub__(self,other):
		x = self.grupo.tabla[(self.elemento, other.grupo.inversos[other.elemento])]
		return element(x, self.grupo)




def Obtener_elementos(g):
	elemts = set()

	for a in g:
		elemts |= set(a[0]) | set(a[1])

	return elemts

def Ver_tabla(g):
	#Se verifica que la tabla es una tabla de multiplicar
	#Es decir, es no vacía
	#Entre cada par de elementos existe la operación
	#Y las operaciones son cerradas
	# Si no se cumple alguna return 0
	# Si todas se cumplen return 1

	elemts = Obtener_elementos(g)

	if g == {}: #Se ve si es vacío
		return 0

	#se ve si cada psoible operación entre par de elementos existe
	prueba = 1
	for a in elemts:
		for b in elemts:
			if (a,b) not in g:
				#si la operación entre a y b no existe pone 0
				prueba = 0
				break
			if g[(a,b)] not in elemts or g[(b,a)] not in elemts: 
				#si no es cerrada pone 0
				prueba = 0
				break
	return prueba



def Ver_neutro(g):
	elemts = Obtener_elementos(g)
	#Ver que el neutro existe

	for a in elemts:
		l=1
		for b in elemts:
			if g[(a,b)] != b or g[(b,a)] != b  :
				l=0
				break
		#if l == 1:
		#	for b in elemts:
		#		if g[(b,a)] != b:
		#			l=0
		#			break
		if l == 1:
			return (a,'si')
	return ('no hay','no')

def Ver_inversos(g):
	elemts = Obtener_elementos(g)
	#Encuentra los inversos
	inverse = {}
	neutro = Ver_neutro(g)[0]

	for a in elemts:
		l=0
		for b in elemts:
			if g[(a,b)]== neutro and g[(b,a)]== neutro:
				inverse[a]=b 
				l=1
		if l==0:
			return (inverse, 'no')
	return (inverse, 'si')

def Ver_grupo(g):
	elemts = Obtener_elementos(g)
	if Ver_tabla(g) == 0:
		return 'No'

	#Ver que es asociativa
	for a in elemts:
		for b in elemts:
			for c in elemts:
				if g[(g[(a,b)],c)] != g[(a,g[(b,c)])]:
					return 'No'

	if Ver_neutro(g)[1] == 'no':
		return 'No'
	if Ver_inversos(g)[1] == 'no':
		return 'No'



	return 'Si'

def Ver_conmutativo(g):
	for a in g.e:
		for b in g.e:
			if g.tabla[(a,b)] != g.tabla[(b,a)]:
				return 'No es conmutativo'
	return 'Es conmutativo'

def Orden_elemento(g, a):
	n=1
	if a not in g.e:
		return 'a no es elemento'

	b=a	
	while b != g.neutro:
		b = g.tabla[(a,b)]
		n+=1

	return n

def Ver_subgrupo(H,G):
	#H es el conjunto de elementos
	#G es el grupo que se verá si es subgrupo de este
	if G.neutro not in H:
		print('No es subgrupo')
		return 0
	for a in H:
		for b in H:
			if (element(a,G)-element(b,G)).elemento not in H:
				print('No es subgrupo')
				return 0
	print(H, 'Es subgrupo')
	

#print(Ver_inversos ({('0','0'):'0',('1','0'):'1',('0','1'):'1',('1','1'):'0'}))
g= Group({('0','0'):'0',('1','0'):'1',('0','1'):'1',('1','1'):'2',
	('1','2'):'0', ('2','1'):'0',('2','2'):'1',('2','0'):'2',('0','2'):'2'})
#print(g.grupo)
#print(g.tabla, g.e, g.neutro, g.inversos, g.grupo)
#print(Ver_conmutativo(g))
#print(Orden_elemento(g,'1'))
a = element('1',g)
b = element('2',g)
print(a-b)

H={'0','2'}

Ver_subgrupo(H,g)
