import os
from subprocess import call

def saludar():
    return "Hola"

def mi_funcion(nombre, apellido): 
    nombre_completo = nombre + " " + apellido 
    print (nombre_completo)

x = "Facundo"
y = "Fernandez"
z = "Mi nombre es %s %s" % (x,y)

mi_funcion("Facundo","Fernandez")

frase = saludar()



call('clear')

print (frase)
print (z)
