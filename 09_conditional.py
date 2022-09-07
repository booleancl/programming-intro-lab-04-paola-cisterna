# expresiones que se pueden evaluar en treminos booleanos
# o dicotonicos
# ejemplo
print(10 > 9)


def is_adult(age):
    if age > 18:
        return True
    else:
        return False

gaby_age = 30
paola_age = 30
# estas siguientes intrucciones las podriamos leer 
# "si(if) el resultado de is_adult ejecutada con la variable gaby_age
# es verdadero, entonces el programa imprime '¿quieres una cerveza'
# de otro modo (else) imprime 'camtemos chuchuwa'?
if is_adult(paola_age):
    print("¿quieres una cerveza?")
else:
    print("cantemos chuchuwa")   

# elif es una abreviacion "else it"nos permite seguir evaluando expresiones. Podemos tener tantos como nesecite 

if (paola_age > gaby_age):
    print("paola es mayor que gaby")
elif paola_age > gaby_age:
    print("paola es menor que gaby")
else:
    print("tienen la misma edad ")
     


