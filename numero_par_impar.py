''' Programa para carlcular si un número entero es par o impar '''

def numParImpar(a):
    num = ''
    if a % 2 == 0:
        num = 'Este número es par'
    else:
        num = 'Este número es impar'
    
    return num

a = int(input('Ingresa un número entero positivo: '))

print(f'El número {a} es {numParImpar(a)}')