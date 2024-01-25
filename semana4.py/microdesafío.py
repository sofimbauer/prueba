# Escribe un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar, debe repetirse
# el proceso hasta que lo introduzca correctamente.

numero_ingresado = 2
while numero_ingresado % 2 == 0:
    numero_ingresado = int(input("Ingrese un número impar:"))
print('Ingresaste un número correcto!')
