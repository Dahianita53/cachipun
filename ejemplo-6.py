""" el juego consiste en que la pc y el jugador tomaran una de las tres opciones.
y el programa determinará quien de los dos ganó o quien perdio o si hubo empate
el juego permite jugar las veces que el jugador desee o hasta que lo finelice"""

import random
import time
from time import sleep


# aca se define elecion de la computadora 
def eleccion_computadora():

    # aca lo que dice es que va a dar una opcion al azar entre el 0 y el 2
    # https://docs.python.org/es/3/library/random.html
    numero_random=random.randint(0,2)

    # aca esta haciendo un array de las opciones que hay
    opciones=["PIEDRA", "PAPEL", "TIJERAS"]

    # aca esta diciendo que x va a poner cualquier opcion al azar entre 0 y 2
    x=opciones[numero_random]
    
    # y aca retorna el valor de x que es una opcion al azar entre el 0 y el 2
    return x

def obtenerResultados(eleccion_pc,eleccion_jugador):
    if(eleccion_pc==eleccion_jugador):
        print("\t\t\t :-v Esto es un empate :-v")
    elif(eleccion_pc=="PIEDRA" and eleccion_jugador=="TIJERAS"):
        print("\t\t\t :-( Perdiste :-(")
    elif(eleccion_pc=="PAPEL" and eleccion_jugador=="PIEDRA"):
        print("\t\t\t :-( Perdiste :-(")
    elif(eleccion_pc=="TIJERAS" and eleccion_jugador=="PAPEL"):
        print("\t\t\t :-( Perdiste :-(")
    elif(eleccion_pc=="PIEDRA" and eleccion_jugador=="PAPEL"):
        print("\t\t\t :-) Ganaste :-)")
    elif(eleccion_pc=="PAPEL" and eleccion_jugador=="TIJERAS"):
        print("\t\t\t :-) Ganaste :-)")
    elif(eleccion_pc=="TIJERAS" and eleccion_jugador=="PIEDRA"):
        print("\t\t\t :-) Ganaste :-)")

print("\t\t\tJUEGO PIEDRA PAPEL O TIJERAS\n Intenta ganar las veces que quieras!!")
x="s"
while x!="n" and x!="N":
    print("Elija una opcion\nPiedra \nPapel \nTijeras")
    eleccion_jugador=input("\tElija una opción->").upper()
    if(eleccion_jugador!="PIEDRA" and eleccion_jugador!="PAPEL" and eleccion_jugador!="TIJERAS"):
      print("\tEsta opción no existe, vuelva a intentar.")
    else:
        print("\t\tTu eleccion fue: \t", eleccion_jugador)
        sleep(0.9)
        eleccion_pc=eleccion_computadora()
        print("\t\tLa computadora elijió: \t", eleccion_pc)
        sleep(0.9)
        obtenerResultados(eleccion_pc,eleccion_jugador)
    x=input("Quieres continuar \ns/n\n->")

print("\t\t\t ¡GRACIAS POR JUGAR!")
K=input()    
