import time
# es perfectamente posible llamar una funcion dentro de otra
# lo hicimos cuando calculamos en volumen de un cilindro.

# pero tambien es perfectamente posible que una funcion se llame a si misma 
# esto es una tecnica muy poderosa para ciertos problemas


# funcion conteo regresivo
# es un funcion que se llama asi misma 
def countdown(number):
    if number <= 0:
        print("kABUMM")
    else:
        print(number)
        time.sleep(0.5)
        countdown(number - 1)
countdown(5) 


def super_sum(number):
    if number <= 0:
        return number 
    else:
         return number + super_sum(number - 1)

print(super_sum(3))

# recursion infinita, sin condicion de salida 
# para nada util, pero entretenida 
def infinite( ):
   infinite()





            