"""
Tarea 6 David Gopar Morales
Muestra de ejemplo programa con excepcionciones
creadas por el usuario

Primeramente le pide digitar dos números y si suman 20
Adivine el siguiente número a salir
"""

# A continuación definimos excepciones
class Error(Exception) :
    pass


class NumerosIncorrectos(Error) :
    """Los numeros son incorrectos"""
    pass


class CharIncorrecto(Error) :
    """Los caracteres son incorrectos"""
    pass

class IncorrectoQ(Exception):
    """
    Nos dice si acertamos en la cantidad de preguntas
    """

    def __init__(self, preguntas,message="No acertaste la cantidad de preguntas"):
        self.preguntas=preguntas
        self.message = message
        super().__init__(self.message)

print("Adivine que quiero...")
while True :
    try:
        n_1 = int(input("Ingrese valor 1 entero : "))
        n_2 = int(input("Ingrese valor 2 entero : "))
        if n_1 + n_2 != 20 :
            raise NumerosIncorrectos
        break

    except NumerosIncorrectos:
        print("Estos valores no suman 20")

print("Diste dos valores que suman 20")

n = 1

print("\nAdivine el número que estoy pensando... ")
print()

while True :
    try:
        n_1=int(input("Ingrese valor entero : "))
        if n_1 != n :
            n+=2
            raise NumerosIncorrectos
        break

    except NumerosIncorrectos:
        print("El valor correcto era:", n-2)

print()
print("Adivinaste el valor que estaba pensando")

print("\nAdivina la letra...")
a = 'w'
while True:
    try:
        letra=str(input("Ingrese una letra :"))
        if a != letra:
            raise CharIncorrecto
        break

    except CharIncorrecto:
        print("Ese no es el caracter")

preguntas = int(input("¿Cua'ntas adivinanzas eran?: "))
if preguntas != 3:
    raise IncorrectoQ(preguntas)

print("Adivinaste todo. Felicidades")
