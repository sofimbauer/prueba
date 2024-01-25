# En la función de nuestro ejercicio hay un fallo potencial,
# averigua cuándo sucede y retorna el valor None en ese caso especial,
# en cualquier otro caso devuelve el resultado normal de la función.
# def dividir(a, b):
# return a/b
# Pista: El fallo es aritmetico y se da por un valor que no podria
# pasarse por el parametro b

def dividir(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None
    # except:
        # return 'Hubo un error'


print(dividir(1, 0))
