# Mis hobbies favoritos
# Crea un programa que pida por teclado (input) los datos de tus tres hobbies
# favoritos y los mismos se guarden en un archivo que se llame
# miHobbieFavorito.txt.

# EXTRA: Hacerlo con un for o un while para no repetir tanto…!!!

hobbies = input('Ingresa tus tres hobbies favoritos (separados): ')
archivo_abierto = open('miHobbieFavorito.txt', 'w')
archivo_abierto.write(hobbies)
archivo_abierto.close()

# v2
# archivo = open('miHobbieFavorito.txt', 'w')
# for i in range(1,4):
#    archivo.write(input('Ingrese su hobbie numero {i}: '))
# archivo.close()
