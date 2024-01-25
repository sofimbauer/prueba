# Crear una Clase Vehiculo de la cual van a heredar la clase Auto
# (del microdesafio) y la clase Lancha (nueva, tiene como atributo
# nombre de motor). Ademas, crear una clase MovimientosEmbarcacion
# de la cual tambien heredara Lancha. Implementar los metodos arrancar,
# tocar_bocina, virar_a_estribor, virar_a_babor y abrir_capot en la clase
# que corresponda. Solo deben mostrar un mensaje que se ejecuto la accion.

class Vehiculo:
    def tocar_bocina(self):
        print('PI PIIIIIIIII')


class MovimientosEmbarcaciones:
    def virar_a_estribor(self):
        print('Has virado a estribor!')

    def virar_a_babor(self):
        print('Has virado a babor!')


class Auto(Vehiculo):
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def abrir_capot(self):
        print('Se abrió el capot!')


class Lancha(Vehiculo, MovimientosEmbarcaciones):
    def __init__(self, nombre_motor):
        self.nombre_motor = nombre_motor


auto1 = Auto('Ford', 'negro')

lancha1 = Lancha('123lol')

print(auto1.marca)
print(auto1.color)
auto1.tocar_bocina()


print(lancha1.nombre_motor)
lancha1.tocar_bocina()
lancha1.virar_a_babor()
lancha1.virar_a_estribor()
