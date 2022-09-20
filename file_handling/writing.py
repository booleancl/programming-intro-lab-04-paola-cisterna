# podemos escribir un archivo con el modo "a"

file = open("file_handling/demo. txt", "a")

file.write("hola inmundo")
file.close()


file = open("file_handling/demo.txt" "w")

file.write("Ooops se borro el contenido anterior")

file.clse()