''' Programa para sumar números flotantes positivos '''

def sumFlotante(a, b):
    sum = a + b
    return sum

a = float(input('Ingresa el primer número flotante: '))
b = float(input('Ingresa el segundo número flotante: '))

print(f'La suma de {a} más {b} es: {sumFlotante(a, b)}')