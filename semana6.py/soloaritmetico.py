# Puede que algunos lo hayan encontrado, pero tomando el ejercicio
# anterior la funcion pareciera no solo que dividir por cero pueda
# generar un error. Que pasa si pasamos strings a nuestra funcion como
# argumento? Deberas acomodar la solucion del microdesafio para que devuelve el
# mensaje “El error encontrado es del tipo:” concatenado con el
# tipo de error que se encontro especifico para cada caso.
# Ejemplo: El error encontrado es del tipo: ZeroDivisionError

def dividir(a, b):
    try:
        return a/b
    except Exception as e:
        return f'El error es del tipo {type(e).__name__}'


print(dividir(1, 0))
print(dividir(1, 'hola'))
print(dividir(1, []))
print(dividir(1, {}))
