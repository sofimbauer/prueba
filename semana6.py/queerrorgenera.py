# Crear un programa que muestre un menu con 4 opciones y,
# segun la opcion elegida por el usuario, muestre el tipo de error que
# se generaria si se ejecutara ese codigo en python.
# Usa las siguientes opciones:
# 1. ‘Soy un string’ - 4
# 2. 4/0
# 3. prnt(‘Mostrando codigo’)
# 4. int(‘Quiero ser un numero’)

opciones = int(input('''Seleccione una opción:
1. 'Soy un string' - 4
2. 4/0
3. prnt('Mostarndo codigo')
4. int('Quiero ser un numero')
Opción seleccionada: '''))

try:
    if opciones == 1:
        print('Soy un string' - 4)
    elif opciones == 2:
        print(4/0)
    # elif opciones == 3:
        # prnt('Mostrando codigo')
    elif opciones == 4:
        print(int('Quiero ser un número'))
    else:
        print('Ingrese una opción válida')
except Exception as e:
    print(f'Se generó un error de tipo {type(e).__name__}')
