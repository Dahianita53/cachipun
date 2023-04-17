"""en este ejemplo puede jugar una vez y te pregunta si quieres
 jugar otra vez o no para elegir debes poner 1, 2 o 3"""

import random

while True:
    aleatorio = random.randrange(0, 3) 
    elijepc = ""
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    opcion = int(input("Elige tu opción "))
    

    if opcion == 1:
         elijeUsuario = "Piedra"
    elif opcion == 2: 
         elijeUsuario = "Papel"
    elif opcion == 3:
         elijeUsuario = "Tijera"
         print("Elejiste: ", elijeUsuario)
         
    
    if aleatorio == 0:
        elijepc = "Piedra"
    elif aleatorio == 1:
        elijepc = "Papel"
    elif aleatorio == 2:
        elijepc = "Tijera" 
        print("La máquina elijio: ", elijepc)
        print("...")
    if elijepc == "Piedra" and elijeUsuario == "Papel":
        print("Ganaste, papel envuelve Piedra")
    elif elijepc == "Papel" and elijeUsuario == "Tijera":
        print("Ganaste, Tijera corta papel") 
    elif elijepc == "Tijera" and elijeUsuario == "Piedra":
        print("Ganaste, Piedra machaca Tijera")
    if elijepc == "Papel" and elijeUsuario == "Piedra": 
        print("perdiste, Papel envuelve Piedra") 
    elif elijepc == "Tijera" and elijeUsuario == "Papel":
        print("perdiste, Tijera corta Papel") 
    elif elijepc == "Piedra" and elijeUsuario == "Tijera":
        print("perdiste, Piedra machaca Tijera") 
    elif elijepc == elijeUsuario:
        print("empate")

    play_again = input("Quieres jugar de nuevo (s/n): ")
    if play_again.lower() != "s":
        break