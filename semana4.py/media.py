# Escribe un programa que pida al usuario cuantos números quiere introducir.
# Luego lee todos los números, guardandolos en una lista,
# y realiza una media aritmética de todos los valores.
# 🖐 Ayuda: Puedes utilizar la funciones sum() entre parentesis
# se le pasa un iterable (lista, tupla, range) y devuelve la suma de
# todos sus elementos (sirve solo con valores numericos)

num = int(input('¿Cuántos números quiere introducir?: '))
lista = []

for iteracion in range(num):
    ingresa = int(input('Ingrese un número: '))
    lista.append(ingresa)
media = sum(lista)/num
print('La media de los valores ingresados es', media)
