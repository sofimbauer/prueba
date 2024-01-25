# Realiza una función separar() que tome una lista de números enteros
# y devuelva dos listas ordenadas.
# La primera con los números pares, y la segunda con los números impares.
# 🖐 Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()

def separar(lista):
    pares = []
    impares = []
    lista.sort()
    for num in lista:
        pares.append(num) if num % 2 == 0 else impares.append(num)
    return pares, impares


p, i = separar([0, 5, 8, 3, 4, 9, 14, 17])
print(p)
print(i)
