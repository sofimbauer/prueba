# Crear un programa que al pasarle una lista de televisores
# devuelva el total a pagar. Tener en cuenta los siguientes puntos
# sobre los televisores:
# 1. Sus atributos son precio base, color, consumo energético
# (letras entre A y F) y peso.
# 2. Los colores disponibles son blanco, negro, rojo, azul y gris.
# 3. Por defecto, el color sera blanco, el consumo energético sera F, el
# precio_base es de 100 $ y el peso de 5 kg.
# 4. Tienen 3 funcionalidades:
#  * Una para comprobar que la letra (consumo energético) es correcta, sino es
# correcta usara la letra por defecto. Se invocara al crear el objeto y sera
# privada.
#  * Otra para comprobar que el color es correcto (no importa si el nombre esta
# en mayúsculas o en minúsculas), sino usa el color por defecto.
# Se invocara al crear el objeto y sera privada al igual que la anterior.
#  * Y la ultima devolvera el precio final del televisor, que aumentara su
# precio según el tamaño y su consumo energético.
# La lista de precios segun tamaño y consumo son:
# Letra | Precio
# A   |   $100
# B   |    $80
# C   |    $60
# D   |    $50
# E   |    $30
# F   |    $10
# Tamaño            | Precio
# Entre 0 y 19 kg   |    $10
# Entre 20 y 49 kg  |    $50
# Entre 50 y 79 kg  |    $80
# Mayor que 80 kg   |   $100
# Probar con los siguientes televisores:
# * precio base 250, color rojo, consumo energético E y peso 10
# * precio base 143, color negro, consumo energético C y peso 13
# * precio base 54, color gris, consumo energético A y peso 7
# * precio base 300, color violeta, consumo energético B y peso 2

class Televisor:
    colores = ['blanco', 'negro', 'rojo', 'azul', 'gris']
    letra_precio = {'A': 100, 'B': 80, 'C': 60, 'D': 50, 'E': 30, 'F': 10}

    def __init__(self, precio_base=100, color='blanco', consumo='F', peso=5):
        self.precio_base = precio_base
        self.color = self.__comprobar_color(color)
        self.consumo = self.__comprobar_consumo(consumo)
        self.peso = peso

    def __comprobar_consumo(self, consumo):
        return consumo if consumo in self.letra_precio.keys() else 'F'

    def __comprobar_color(self, color):
        return color if color.lower() in self.colores else 'blanco'

    def precio_final(self):
        if 0 <= self.peso <= 19:
            precio_tamanio = 10
        elif 20 <= self.peso <= 49:
            precio_tamanio = 50
        elif 50 <= self.peso <= 79:
            precio_tamanio = 80
        elif 80 <= self.peso:
            precio_tamanio = 100
        precio_consumo = self.letra_precio.get(self.consumo)
        return self.precio_base + precio_consumo + precio_tamanio


def calcular_precio_total(listado_televisores):
    precio_total = 0
    for tele in listado_televisores:
        precio_total += tele.precio_final()
    return precio_total


televisores = [
    Televisor(250, 'rojo', 'E', 10),
    Televisor(143, 'negro', 'C', 13),
    Televisor(54, 'gris', 'A', 7),
    Televisor(300, 'violeta', 'B', 23)
]

print(calcular_precio_total(televisores))
