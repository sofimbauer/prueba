# Solicitar al usuario la cantidad de numeros enteros a sumar.
# Luego permitirle ingresarlos uno por uno hasta que se ingresen
# todos o el usuario escriba la palabra ‘exit’.
# El programa debe validar que se ingreso ‘exit’ y dejar de solicitar numeros.
# Finalmente, el algoritmo debe mostrar la suma obtenida con un mensaje que
# resalte si fue total la carga de datos o parcial
# (debido al ingreso de ‘exit’).

num = int(input('¿Cuántos números enteros quiere sumar?:  '))

suma = 0
for iteracion in range(num):
    entrada = input('Ingrese un número entero o la plabra exit: ')
    if entrada.lower() == 'exit':
        print(f'La suma obtenida fue de {suma} con una carga de datos parcial')
        break
    suma += int(entrada)
else:
    print(f'La suma da {suma} con una carga de datos total')
