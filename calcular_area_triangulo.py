''' Programa para calcular el área de un triangulo '''
''' donde a es la altura y b la base'''

def areaTriangulo(a, b):
    area = (b * a) / 2
    return area

a = float(input('Ingresa la altura del triangulo: '))
b = float(input('Ingresa la base del triangulo: '))

print(f'La altura del triangulo es: {a}, la base del triangulo es: {b} por lo tanto el área es: {areaTriangulo(a, b)}')