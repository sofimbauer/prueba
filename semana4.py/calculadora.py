# Escribe un programa que lea dos números por teclado y permita
# elegir entre 4 opciones en un menú:
# 1. Mostrar una suma de los dos números
# 2. Mostrar una resta de los dos números (el primero menos el segundo)
# 3. Mostrar una multiplicación de los dos números
# 4. Si elige esta opción se interrumpirá la impresión del menú
# y el programa finalizará
# 5. En caso de no introducir una opción válida,
# el programa informará de que no es correcta.

num_1 = int(input('Ingrese un número: '))
num_2 = int(input('Ingrese un número: '))

bandera = True
while bandera:  # O puedo poner directamente True o 1 (que es True)
    opcion = int(input('''Seleccione una opción:
1. Suma de los dos números
2. Resta de los dos números
3. Multiplicación de los dos números
4. Salir
Opción seleccionada: '''))
    if opcion == 1:
        print(f'La suma de los dos números es {num_1 + num_2}')
    elif opcion == 2:
        print(f'La resta de los dos números es {num_1 - num_2}')
    elif opcion == 3:
        print(f'La multiplicación de los dos números es {num_1*num_2}')
    elif opcion == 4:
        print('Vuelva pronto')
        # bandera = False
        break
    else:
        print('No es una opción válida. Vuelva a intentarlo')
