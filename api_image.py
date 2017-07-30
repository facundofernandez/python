import os
import shutil
import sys
from librerias.clear import cls
#from urllib2 import urlopen
from urllib.request import urlopen

#limpio pantalla
cls()

url = "http://lorempixel.com"
tipos = ["abstract","animals","business","cats","city",
        "food","night","life","fashion","people","nature",
        "sports","technics","transport"]
directorio_img = "imagenes"

if len(sys.argv) == 1:
    ancho = input("Ancho: ")
    alto = input("Alto: ")
else:
    ancho = sys.argv[1]
    alto = sys.argv[2]


print( "Seleccione tipo de imagen: " )
for index,item in enumerate( tipos ):
    print("%d - %s" % ( index,item ) )
tipo = input( "Tipo de imagen:" )
cantidad = int( input( "Cantidad de imagenes: " ) )

#si existe directorio lo borro con todos sus archivos
if os.path.exists( directorio_img ):
    shutil.rmtree( directorio_img )

os.mkdir( directorio_img )

    

for img in range(cantidad):
    url_req = "%s/%s/%s/%s" % (url,ancho,alto,tipos[int(tipo)])
    resultado = urlopen(url_req)
    lectura = resultado.read()
    f= open( directorio_img + "/imagen_%d.jpg" % img,"wb")
    f.write(lectura)
    f.close()


#limpio pantalla
cls()
