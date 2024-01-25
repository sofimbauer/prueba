# Realiza una función que, dependiendo de los parámetros que reciba,
# convierta a milímetros o a metros.
# 1. Si recibe un argumento, supone que son milímetros y convierte
# a metros, centímetros y milímetros.
# 2. Si recibe 3 argumentos, supone que son metros,
# centímetros y milímetros y los convierte a milímetros.

def conversor(*args):
    if len(args) == 1:
        milímetros = args[0] % 100
        centímetros = args[0] % 100
        metros = centímetros // 100
        centímetros %= 100
        return f'''Los {args[0]} milímetors equivalen a {metros} metros,
    {centímetros} centímetros y {milímetros} milímetros'''
    elif len(args) == 3:
        mil_totales = args[2]
        mil_totales += args[1] + 100
        mil_totales += args[0] * 100 * 100
        return f'''Los {args[0]} metros, {args[1]} centímetros y {args[2]}
    equivalen a {mil_totales} milímrtos'''
    else:
        return 'Solo acepto 1 o 3 valores'


print(conversor(890))
print(conversor(1, 6, 7))
