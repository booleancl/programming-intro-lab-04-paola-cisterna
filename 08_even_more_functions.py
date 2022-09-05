# las funciones pueden hacer cosas y tambien pueden retornar valores

def circle_area(radius):
    area = 3.1415*radius**2
    return area

# en este caso la funcion me entrega o devuelve un valor 

result = circle_area(4)
print(result)
def circle_volume(radius,height):
    volume = 3.1415*radius**2*height
    return volume
result_two = circle_volume(4,10)
print (result_two)    