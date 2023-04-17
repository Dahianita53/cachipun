"""este ejemplo lo que hace es que te pide tu nombre y va contando las veces que ganas
y tambien te pide cuantas rondas quieres jugar para elegir debes escribir piedra, papel o tijeras"""

import random 

print("**************************")
print("* Piedra Papel o Tijeras *")
print("**************************")

print()

print("*******************")
nombre = input("Ingresa tu nombre: ")
print("*******************")


rondas = int(input(nombre + ", cuantas rondas quieres jugar: "))

opciones = ['piedra','papel','tijeras']

puntosusuario = 0
puntoscomputadora = 0


while rondas > 0: 
    usuario = input(nombre + ", escoje piedra, papel, o tijeras: ").lower()
    computadora = random.choice(opciones)
    if (usuario == "piedra" and computadora == "tijeras") or (usuario == "papel" and computadora == "piedra") or (usuario == "tijeras" and computadora == "piedra"):
        print("Ganaste")
        puntosusuario += 1
    elif (usuario == "piedra" and computadora == "papel") or (usuario == "papel" and computadora == "tijeras") or (usuario == "tijeras" and computadora == "papel"):
        print("Perdiste")
        puntoscomputadora += 1
    elif usuario == computadora:
        print("Empate")
        puntoscomputadora += 0
        puntosusuario += 0
    else:
        print("Duelo no encontrado")
        rondas += 1
    rondas -= 1
    print("Te quedan " + str(rondas) + ", animos vamos a ganar")
    print(nombre + " " + str(puntosusuario) + " : " +  str(puntoscomputadora) + " computadora")
    
if puntosusuario > puntoscomputadora:
    print("El duelo quedo a favor del humano/a " + nombre + ", con un marcador de " + str(puntosusuario) + " : " + str(puntoscomputadora))
    print("Felicidades, Ganaste el juego")
elif puntosusuario == puntoscomputadora:
    print("El duelo quedo en empate, con un marcador de " + str(puntosusuario) + " : " + str(puntoscomputadora))
    print("Empate, un duelo muy parejo")
else:
    print("El duelo quedo a favor de la computadora, con un marcador de " + str(puntosusuario) + " : " + str(puntoscomputadora))
    print("Perdiste, vuelve a intentarlo")

print()

print("***********")
print("* End game *")
print("***********")