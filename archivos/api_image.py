_author__ = "Facundo Fernandez"
__version__ = "1.0.0"
__email__ = "ff.fernandez.facundo@gmail.com"

'''Script para crear imagenes aleatorias de diferentes temas
    1) Se ingresara Ancho, Alto, tipo de imagen y cantidad de img 
    2) Se utiliza la web http://lorempixel.com para generar las imagenes
    3) Se crea un directorio llamado imagenes donde las colocara
'''
# -*- coding: utf-8 *-* 

import os
import shutil
import sys
from urllib.request import urlopen
from librerias.funciones import cls

#limpio pantalla
cls()

url = "http://lorempixel.com"
tipos = ["abstracto", "animales", "negocios", "gatos", "ciudad", "comida", "noche", 
         "vida", "moda", "personas", "naturaleza", "deportes", "technics", "transporte"]
         
directorio_img = "img"

if len(sys.argv) == 1:
    ancho = input("Ancho: ")
    alto = input("Alto: ")
    cls()
else:
    ancho = sys.argv[1]
    alto = sys.argv[2]
    directorio_img = sys.argv[3]
    tipo = sys.argv[4]


print( "Seleccione tipo de imagen: " )

for index, item in enumerate(tipos):
    print("%d - %s" % (index, item))

tipo = input("Tipo de imagen: ")
cls()

cantidad = int(input("Cantidad de imagenes: "))
cls()
print("Procesando imagenes, por favor espere...")
#si existe directorio lo borro con todos sus archivos
if os.path.exists(directorio_img):
    shutil.rmtree(directorio_img)

os.makedirs(directorio_img) #creo directorio donde se guardan

#Creo imagen deacuerdo a las opciones y la guardo en la carpeta
for img in range(cantidad):
    url_req = "%s/%s/%s/%s" % (url, ancho, alto, tipos[int(tipo)])
    resultado = urlopen(url_req)
    lectura = resultado.read()
    f = open(os.path.join(directorio_img, "imagen_%d.jpg" % img), "wb")
    f.write(lectura)
    f.close()


#limpio pantalla
cls()
