# Escribir una función que reciba una muestra de números en una
# lista y devuelva su media.

def calcular_media(valores):
    return sum(valores) / len(valores)


media = calcular_media([1, 4, 8, 16, 9])
print('La media de la muestra de números es', media)
