''' Programa para calcular el factorial de un número entero positivo '''

def factorial(a):
    fact = 1
    for i in range(1, a + 1):
        fact = fact * i
    return fact
    
a = int(input('Ingresa un número entero positivo para calcular su factorial: '))

print(f'El factorial de {a} es: {factorial(a)}')