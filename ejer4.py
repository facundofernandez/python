import os


print( os.path.exists("imagenes") )

if not os.path.exists("imagenes"):
    os.mkdir("imagenes")

help(os)