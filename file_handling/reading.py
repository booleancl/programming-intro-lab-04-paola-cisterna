# modos para leer un archivo co la funcion open ()

# "r"para leer
# "a"para agregar al final (append)
# "w" para sobre escribir el contenido

file = open('file_handling/sample.txt', "r")

#la funcion open entrega un "objeto", entenderemos un objeto
# como algo que tiene "datos"y "metodos",los metodos son para
#manipular sus datos 

print(file)

#para leer el contenido file, tenemos 
#read()

print(file.read ())

# podemos leer el archivo utilizando for 
file = open('file_handling')    

for line in file:
    print(line)

# luego de utilizar el archivo 




