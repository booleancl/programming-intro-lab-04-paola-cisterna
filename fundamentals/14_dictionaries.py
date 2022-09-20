# similar a los arreglos los diccionarios nos permiten estructurar informacion con la diferencia de que los elementos estan ordenados por llave y no por indice


my_car = {
    "brand": "mazda",
    "model": "5",
    "year": 2022,
    "options":["5puertas", "aire acondionado", "frenos abs"],
    "available": True

}

print(my_car["brand"])
print(my_car["year"])
print(my_car["options"])

# si queremos todas las llaves tenemos el metodo .keys()
print(my_car.keys())
# si queremos todos los valores, tenemos el metodo .values()
print(my_car.values())
# podemos tambien actualizar valores de una determinada llave 

my_car["model"] = "9"
print(my_car["model"])

# tambien podemos arreglar llaves y valores
my_car["color"] = "silver"
print(my_car)