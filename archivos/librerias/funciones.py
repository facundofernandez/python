import os

def cls():
    '''Limpia Pantalla independiente del SO  '''
    os.system('cls' if os.name=='nt' else 'clear')
