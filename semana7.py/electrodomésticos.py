# Ahora cambiemos la clase Televisor a Electrodomestico y creemos una nueva
# clase Televisor y otra Lavadora que hereden de Electrodomestico. Estas nuevas
# clases deberan, ademas de cumplir con lo heredado, agregar lo siguiente:
# El Televisor:
# * Tener los atributos “resolucion” (float, por defecto 20 pulgadas) y
# “sintonizador TDT” (booleano, por defecto False);
# * Y, al precio final, si tiene una resolución mayor de 40 pulgadas, se
# incrementara el precio un 30% y si tiene un sintonizador TDT incorporado,
# aumentara $50
# La Lavadora:
# * Tener el atributo carga (float, por defecto 5 kg);
# * Y, al precio final, si tiene una carga mayor de 30 kg,
# aumentara el precio $50

class Electromedistico:
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


class Televisor(Electromedistico):
    def __init__(self, precio_base=100, color='blanco', consumo='F', peso=5,
                 resolucion=20, sintonizador_TDT=False):
        super(self).__init__(precio_base, color, consumo, peso)

    # v2
    # def __init__(self, resolucion=20, sintonizador_TDT=False, *args,
    # **kwargs):
    # super(self).__init__(*args, **kwargs)

    def precio_final(self):
        extras = 0
        if 40 < self.resolucion:
            extras *= 1.3
        if self.sintonizador_TDT:
            extras += 50
        return super(self).precio_final()


class Lavadora(Electromedistico):
    def __init__(self, precio_base=100, color='blanco', consumo='F',
                 peso=5, carga=5):
        super(self).__init__(precio_base, color, consumo, peso)

    # v2
    # def __init__(self, carga=5, *args, **kwargs):
    # super(self).__init__(*args, **kwargs)

    def precio_final(self):
        extras = 0
        if 30 < self.carga:
            extras += 50
        return super(self).precio_final()
