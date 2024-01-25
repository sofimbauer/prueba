# Descripción de la actividad.
# Utilizando la función range() y la conversión a listas,
# genera las siguientes listas dinámicamente:
# - Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# - Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# - Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# - Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
# - Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
# 🖐 Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))

lista_1 = list(range(11))
print('Lista 1: ', lista_1)
lista_2 = list(range(-10, 1))
print('Lista 2: ', lista_2)
lista_3 = list(range(0, 21, 2))
print('Lista 3: ', lista_3)
lista_4 = list(range(-19, 0, 2))
print('Lista 4: ', lista_4)
lista_5 = list(range(0, 51, 5))
print('Lista 5: ', lista_5)
