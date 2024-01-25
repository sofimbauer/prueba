from datetime import datetime

dia = int(input('Ingrese su día (número) de cumpleaños: '))
mes = int(input('Ingrese su mes (número) de cumpleaños: '))
anio = int(input('Ingrese su año (número) de cumpleaños: '))

hoy = datetime.now()
nacimiento = datetime(anio, mes, dia)

tiempo = hoy - nacimiento
print(tiempo)
anios = tiempo.days // 365
meses = (tiempo.days % 365) // 30
dias = (tiempo.days % 365) % 30
horas = tiempo.seconds // 3600
minutos = (tiempo.seconds % 3600) // 3600
segundos = (tiempo.seconds % 3600) % 3600

print(f'''Tenes {anios} años, {meses} meses,
      {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos''')

proximo = datetime(hoy.year + 1, mes, dia)
(proximo - hoy).total_seconds

print(f'Faltan {(proximo - hoy).total_seconds()} seg para tu cumpleaños.')
