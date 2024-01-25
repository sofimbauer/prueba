# Trabajando con variables podriamos guardar datos sueltos
# como los siguientes y mostrarlos

# nombre = 'Juan'
# edad = 26
# print(nombre)
# print(edad)

#  Pero para crear mas cantidad con lo que sabemos tendrimos un monton
# de variables nombre y edad, ademas de que no se relacionan entre
# si mas que por algo que pongamos en el nombre de la variable

# nombre1 = 'Juan'
# edad1 = 26
# nombre2 = 'Pepe'
# edad2 = 21
# print(nombre1, edad1)
# print(nombre2, edad2)

# entonces podriamos usar diccionarios y agruparlos un poco mas

# persona1 = {
# 'nombre' : 'Juan',
# 'edad' : 26
# }
# persona2 = {
# 'nombre' : 'Pepe',
# 'edad': 21
# }

# print(persona1['nombre'])
# print(persona1['edad'])
# print(persona2['nombre'])
# print(persona2['edad'])


# Pero si tiene mas datos o tenemos que crear varias personas mas serian un
# monton de lineas para cada persona. Y aca entra una clase (por lo menos
# un ejemplo simple y basico de mejora en relacion
# a todo lo que nos brindan las clases)

class Persona:
    '''
    Esta es una clase donde se agregan todos los datos
    respecto a una persona
    '''
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


persona1 = Persona('Juan', 26)
type(persona1)
persona2 = Persona('Pepe', 21)
print(persona1.nombre)
print(persona1.edad)
print(persona2.nombre)
print(persona2.edad)
