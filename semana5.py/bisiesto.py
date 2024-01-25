# Realizar una función llamada año_bisiesto que le permita al usuario
# ingresar un año y verificar si es o no bisiesto:
# - Recibirá un año por parámetro (el usuario lo ingresara por un input )
# - Imprimirá “El año año es bisiesto” si el año es bisiesto
# - Imprimirá “El año año no es bisiesto” si el año no es bisiesto
# - Si se ingresa algo que no sea número, debe indicar que
# se ingrese un número.
# Información a tener en cuenta:
# Se recuerda que los años bisiestos son múltiplos de 4, pero
# los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.
# Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no
# es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.


def anio_bisiesto(anio):
    for caracter in anio:
        if caracter not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('Debes ingresar un número!')
            return
    if int(anio) % 4 == 0 and (int(anio) % 100 != 0 or int(anio) % 400 == 0):
        print(f'El año {anio} es bisiesto')
    else:
        print(f'El año {anio} no es bisiesto')


anio_bisiesto(input('Ingrese un año: '))
