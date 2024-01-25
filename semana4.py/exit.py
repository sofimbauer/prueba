# Solicitar al usuario numeros enteros para sumarlos.
# Para finalizar la ejecución del programa, el usuario debe escribir
# la palabra exit.
# El programa debe validar dicha acción y dejar de solicitar numeros.
# Finalmente, el algoritmo debe mostrar la suma obtenida.

bandera = True
suma = 0
while bandera:
    entrada = input('Ingrese un número entero o la plabra exit: ')
    if entrada.lower() == 'exit':
        bandera = False
    else:
        suma += int(entrada)
print(f'La suma da {suma}')
