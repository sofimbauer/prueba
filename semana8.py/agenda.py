# Agenda de contactos
# Crear un menu con las opciones de agendar contacto y ver informacion de
# contacto. Para agendar se solicitara al usuario un: nombre, apellido,
# telefono, direccion. Para ver informacion se pedira el nombre y apellido.
# La informacion sera un listado de diccionarios, donde cada diccionario
# tendra como claves lo solicitado al usuario y como valor lo que ingrese el
# usuario. A su vez, este listado debe estar guardado en un archivo json.

'''
[
    {nombre: 'nombre',
     dni: 123
    },
    {nombre: 'nombre',
     dni: 345
    },
    {nombre: 'nombre',
     dni: 12345
    }
]
'''
import json


def agendar():
    nombre = input('Ingrese su nombre: ')
    dni = input('Ingrese su dni: ')
    try:
        archivo_abierto_lectura = open('datos.json', 'r')
        datos = json.load(archivo_abierto_lectura)
        archivo_abierto_lectura.close()
    except ZeroDivisionError:
        datos = []
    datos.append({'nombre': nombre, 'dni': dni})
    archivo_abierto_escritura = open('datos.json', 'w')
    json.dump(datos, archivo_abierto_escritura, indent=4)
    archivo_abierto_escritura.close()


def ver_contacto():
    nombre = input('Ingrese su nombre: ')
    with open('datos.json', 'r') as archivo_abierto_lectura:
        datos = json.load(archivo_abierto_lectura)
        for dato in datos:
            if dato['nombre'] == nombre:
                print(dato['dni'])


def menu():
    print('''Menu
          1. Agendar contacto.
          2. Ver contacto.
          ''')
    opcion = input('Ingrese opcion: ')
    if opcion not in ['1', '2']:
        print('No ingreso ninguna opcion valida.')
        return
    if opcion == '1':
        agendar()
    elif opcion == '2':
        ver_contacto()


menu()
