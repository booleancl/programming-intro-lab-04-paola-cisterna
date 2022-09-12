mano1 = int(input("jugador1\n"))
mano1_eleccion = opciones[mano1 - 1]
option = ["piedra", "tijera", "papel",]

mano_computador = random.choice(opciones)

print("Mi mano: ", mano1_eleccion)
print("Mano del computador:", mano_computador)

if (mano1_eleccion == mano_computador):
  print("Empatan jugadores")
user_input = int(input("jugador\n"))
user_option = options[user_input - 1]

computer_option = random.choice(option)

print("mi mano:", user option)
print("mano del computador:",computer_option)

elif (mano1_eleccion == "piedra" and mano_computador == "tijera") or(mano1_eleccion == "tijera" and mano_computador == "papel") or (mano1_eleccion == "papel" and mano_computador == "piedra"):
  print("Felicitaciones! ganaste la partida")
    
else:
    print("Lo siento! el computador ha ganado")




