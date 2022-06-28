#! ./venv/bin/python3.8
# -- coding: utf-8 --
"""
David Gopar Morales

Tarea 13.
Entrega: Jueves 16 de junio

Escriba un programa que descargue de alguna fuente como yahoo-finance, bloomberg,
investing, etc, la cotización del dólar-peso (usd/mxn). El programa debe
ejecutarse de manera permanente y exactamente a las 7, 8, 9, ..., 15 y 16 horas
de todos los días debe descargar la cotización y agregarla junto con la hora y
fecha a un archivo csv.

Sugerencias.

1. Mientras el programa no deba descargar ninguna información use el
método sleep del módulo time para ponerlo a dormir.
(https://realpython.com/python-time-module/)

2. Para descargar la información de páginas web use el módulo requests
(https://realpython.com/python-requests/)

3. Para analizar el código html de una página use la biblioteca beautiful soup
(https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/)


No se pudo utilizar la página de Yahoo pues la clase donde contiene el precio cambia
constantemente.
Y no se usó la página de banxico pues sólo muestra un precio fijo al día

"""

import csv
import datetime
import requests
from time import sleep
from bs4 import BeautifulSoup

URL = "https://www.google.com/finance/quote/USD-MXN"

ACTUAL = datetime.datetime.now()
DELTA = 60*60 - (ACTUAL.minute*60 + ACTUAL.second)
# Se espera hasta que esté en una hora exacta, sin 
# minutos: 7:00:00, ... ,10:00:00 , etc. 
if DELTA != 60*60:
 	sleep(DELTA)

while True:

	ACTUAL = datetime.datetime.now()

	if ACTUAL.hour < 7 :
		#Se espera hasya que sean las siete
		sleep(7*60*60 - (ACTUAL.hour*60*60 + ACTUAL.minute*60 + ACTUAL.second))

	ACTUAL = datetime.datetime.now()
	while 7 <= ACTUAL.hour <= 16:
		pagina = requests.get(URL)
		soup = BeautifulSoup(pagina.content, 'html.parser')
		
		# Debido a que en esta página es la primera clase que se llama así
		# no es necesario hacer todo el árbol de búsqueda

		dolar = soup.find('div', class_="YMlKec fxKbKc").text
		with open("dolar-peso.csv", "a", newline="") as archivo:
			archivo_writer = csv.writer(archivo)
			archivo_writer.writerow([dolar, ACTUAL])
			archivo.close()
		#Para evitar retraso se actualiza ACTUAL
		ACTUAL = datetime.datetime.now()
		sleep( 60*60 - (ACTUAL.minute*60 + ACTUAL.second))
		ACTUAL = datetime.datetime.now()

	# La siguiente asignación de ACTUAl
	# no es tan necesario, pero para ser mas exactos en el tiempo la dejamos
	ACTUAL = datetime.datetime.now()
	if ACTUAL.hour > 16 :
		sleep( 24*60*60 - (ACTUAL.hour*60*60 + ACTUAL.minute*60 + ACTUAL.second ))
