''' Programa para control de una veterinaria '''

# Registro de pacientes (nombre, edad, peso)

def registrarPacientes(num_pacientes: int) -> list[dict]:
    ''' Registrar pacientes '''
    pacientes = []
    for i in range(1, num_pacientes + 1):
        nombre = input(f'Nombre del paciente {i}: ')
        while True:
            try:
                edad = int(input(f'Edad del paciente {i} (en años): '))
                if edad < 0:
                    print('La edad no puede ser negativa. Intente de nuevo.')
                    continue
                break
            except ValueError:
                print('Entrada invalida. Intente de nuevo.')
        while True:
            try:
                peso = float(input(f'Peso del paciente {i} (en kg): '))
                if peso < 0:
                    print('El peso no puede ser negativo. Intente de nuevo.')
                    continue
                break
            except ValueError:
                print('Entrada invalida. Intente de nuevo.')
        pacientes.append({
            "nombre": nombre,
            "edad": edad,
            "peso": peso
        })
    return pacientes

def mascotaMasPesada(pacientes: list[dict]) -> dict:
    ''' Encontrar la mascota más pesada '''
    mascota_pesada = max(pacientes, key=lambda x: x['peso'])
    return mascota_pesada

def promedioEdad(pacientes: list[dict]) -> float:
    ''' Calcular el promedio de edad de las mascotas '''
    total_edad = sum(p['edad'] for p in pacientes)
    promedio = total_edad / len(pacientes)
    return promedio

def clasificaciónEdad(edad: int) -> str:
    ''' Clasificar la edad de la mascota '''
    if edad < 1:
        return 'Cachorro'
    elif 1 <= edad <= 7:
        return 'Adulto'
    else:
        return 'Senior'

def main():
    while True:
        try:
            num_pacientes = int(input('Número de pacientes a registrar: '))
            if num_pacientes < 1:
                print('Debe ser un número mayor a 0')
                continue
            break
        except ValueError:
            print('Entrada invalida. Intente de nuevo.')
    
    pacientes = registrarPacientes(num_pacientes)
    mascota_pesada = mascotaMasPesada(pacientes)
    edad_promedio = promedioEdad(pacientes)

    print('--- Reporte de la Veterinaria ---')
    print(f'Los pacientes registrados son: {pacientes}')
    print(f'La mascota más pesada es: {mascota_pesada["nombre"]} con {mascota_pesada["peso"]} kg')
    print(f'El promedio de edad de las mascotas es: {edad_promedio} años')
    # clasificación de cada mascota por nombre
    for p in pacientes:
        clasificacion = clasificaciónEdad(p['edad'])
        print(f'La mascota {p["nombre"]} es clasificada como: {clasificacion}')
    
if __name__ == "__main__":
    main()