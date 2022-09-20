# los arreglos (listas) son una estrcuctura de datos fundamental
# que permite agrupar valores, separados por coma

first_array = ['sacar la basuera','dormir', 'peinarse','secar la ropa']
# en python el primer elemento de un arreglo tiene posicion (indice) 0
print(first_array[0])
print(first_array[1])
print(first_array[2])
print(first_array[3])

# no existe el elemento con indice 4 y python da un error
# print(first_array[4])

# podemos saber el largo de un arreglo o lista con la funcion pre definida len()

print(len(first_array))

# ademas, podemos agregar elementos al finalde arreglo con el metodo append
first_array.append('comer')
first_array.append('dormir')

# podemos indicar la posicion del nuevo elemento a agregar con insert
first_array.insert(0,'levantarse')


# podemos imprimir la lista completa 
print(first_array)

