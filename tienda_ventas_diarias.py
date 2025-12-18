''' Programa para calcular las ventas diarias de una tienda (una semana)'''

def ventasDiarias(dias: int) -> list[float]:
    ''' Calcular venta total '''
    ventas = []
    for d in range(1, dias + 1):
        while True:
            try:
                venta = float(input(f'venta del día {d}: '))
                if venta < 0:
                    print('La venta no puede ser negativa. Intente de nuevo.')
                    continue
                ventas.append(venta)
                break
            except ValueError:
                print('Entrada invalida. Intente de nuevo.')
    return ventas

def analizarVentas(ventas: list[float]):
    ''' Total vendido '''
    total_ventas = sum(ventas)
    ''' Promedio diario vendido '''
    dias_venta = len(ventas)
    promedio_diario = total_ventas / dias_venta
    ''' Día con mayor venta '''
    dia_mayor_venta = ventas.index(max(ventas)) + 1
    '''Día con menor venta '''
    dia_menor_venta = ventas.index(min(ventas)) + 1

    return {
        "total_ventas": total_ventas,
        "promedio_diario": promedio_diario,
        "dia_mayor_venta": dia_mayor_venta,
        "dia_menor_venta": dia_menor_venta,
    }

def main():
    while True:
        try:
            dias = int(input('Dias de ventas que desea ingresar: '))
            if dias < 1:
                print('Debe ser un número mayor a 0')
                continue
            break
        except ValueError:
            print('Entrada invalida. Intente de nuevo.')
    
    ventas = ventasDiarias(dias)
    res = analizarVentas(ventas)

    print(f'Las ventas registradas son: {ventas}')
    print(f'El total de las ventas generadas es: {res['total_ventas']}')
    print(f'El promedio diario de venta es de: {res['promedio_diario']}')
    print(f'El día con mayor venta fue el día: {res['dia_mayor_venta']}')
    print(f'El día con menor venta fue el día: {res['dia_menor_venta']}')
    

if __name__ == "__main__":
    main()    