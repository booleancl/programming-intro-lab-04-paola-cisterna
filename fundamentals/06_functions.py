# una funcion es un grupo de setencias con un nombre que realiza una computacion
# primero uno define una funcion y luego se "llama" esa funcion 

# Python   viene con muchas funciones listas para usar. 
# Solo hay que llamarlas o ejecutarlas 
print("hola pao")

# la mayoria de las funcuiones entregan un valor,   es decir,nos devuelven el resultado: ejemplo

str_num = '32'
real_num = int(str_num) #esta funcion transforma a enteros 
print(type(str_num))

float_num = 3.9999
int_num = int(float_num)
print(int_num)

# la siguiente linea es un error 
# int(hola inmundo)

print(float('32')) # esta funcion entrega un float
print(str(3.1415)) # esta funcion enrega str

#composicion de funciones: anidar funciones 

print(str(3.1415))