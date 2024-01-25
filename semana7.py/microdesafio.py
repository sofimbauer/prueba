# Crear una clase Auto que contenga 2 atributos de instancia.
# Con esta clase crear un auto y mostrar los datos del auto creado.

class Auto:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def bocinazo(self):
        print('PI PIIIIIII')


auto1 = Auto("Ford", "rojo")

print(auto1.marca)
print(auto1.color)
auto1.bocinazo()
