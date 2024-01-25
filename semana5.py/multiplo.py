# Crea un programa que le pida dos números enteros
# al usuario y diga por consola, si alguno de ellos es múltiplo del
# otro. La función debe llamarse es_multiplo().

def es_multiplo(num_1, num_2):
    if num_1 % num_2 == 0:
        print(f'{num_1} es múltiplo de {num_2}')
    elif num_2 % num_1 == 0:
        print(f'{num_2} es múltiplo de {num_1}')
    else:
        print(f'{num_1} no es múltiplo de {num_2}, ni viceversa')


# numero1 = int(input('Ingrese el primer número: '))
# numero2 = int(input('Ingrese el segundo número: '))
# es_multiplo(numero1, numero2)

es_multiplo(5, 9)
