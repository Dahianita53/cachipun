"""este ejemplo lo que hace es que te da a elegir entre piedra, papel o tijera y para 
elegir debe poner 1, 2 o 3"""

from random import randint

def juego(opc):
    opciones = ["piedra", "papel", "tijeras"]

    ia = opciones[randint(0,2)]
    
    if ia == opc:
        print("Empate elijieron lo mismo")
        
    elif ia == "piedra":
        
        if opc == "papel":
            print("Ganaste, Papel le gana a Piedra")
        else:
            print("Perdiste, Piedra le gana a Tijeras")
            
    elif ia == "papel":
        
        if opc == "tijeras":
            print("Ganaste, Tijeras le ganan a Papel")
        else:
            print("Perdiste, Papel le gana a Piedra")
    
    else:
        
        if opc == "piedra":
            print("Ganaste, Piedra le gana a Tijeras")
        else:
            print("Perdiste, Tijeras le ganan a Papel")
  
ppt = {1:"piedra",2:"papel",3:"tijeras"}    

opc = int(input("""Elije una opción:
1) Piedra
2) Papel
3) Tijeras \n>> """))

juego(ppt[opc])