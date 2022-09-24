# podemos crear o definir nuestras propias funciones 
#lo hacemos con la palabra especial "def"y el cuerpo
# la funcion debe ir correctamente identado

def chuchuwa(inst):
    print("chuchuwa chuchuwa chuchuwa wa wa!")
    print("chuchuwa chuchuwa chuchuwa wa wa!")
    print("atencion!, compañia:")
    print(inst)
 
print(chuchuwa)
print(type(chuchuwa))
# el llamado de la funcion 

chuchuwa("mano hacia el frente" )
chuchuwa("hombros hacia atras")
# funciones deben llamarse o ejecutarse con los mismos parametros que se definio 

result = chuchuwa("lengua afuera")

# si la funcion no tiene un valor de retorno, nos entregara "none", que es para representar: "nada"
print(result) 
