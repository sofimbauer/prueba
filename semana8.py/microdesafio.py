class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f'{self.nombre} y {self.nota}')


def gritar():
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAA!')
