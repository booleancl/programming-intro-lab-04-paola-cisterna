
print("bienvenido al programa")
user_input = ""

while user_input != "exit":
    print("##############")
    print("ingresa una opcion")
    print("1","agregar contenido")
    print("2", "leer contenido")
    print("exit", "para salir")
    print("################")

    user_input = input()
    
    if user_input == "1":
         file = open("demo_two.txt","a")
         user_content = input("ingresa el contenido")
         file_write(user_content + "\n")
         file.close()

    elif user_input == "2":
         file = open ("demo_two.txt", "r" )
         for line in file:
             print(line)
    else:
         print("opcion incorrecta")

print("chau chau")
