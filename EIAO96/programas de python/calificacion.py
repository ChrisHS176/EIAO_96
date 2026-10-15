
while True:
    try:
        numero = int(input("¿Cúantas calificaciones deseas ingresar?"))
        if numero <= 0:
            print("Error: Ingresa un número mayor a 0")
        else:
            break
    except Exception as e:
        print("Error: Ingresa un número valido")
aprobado = 0
reprobado = 0
suma = 0
alta = 0
baja = 0
for i in range(numero):
    while True:
        try:
            calificacion = int(input(f'Ingresa la calificación número: '))
            if numero <= 0:
                print("Error: Ingresa un número mayor a 0")
            else:
                break
        except ValueError:
            print("Error: Ingrese un número valido")
    if calificacion >= 70:
        aprobado += 1
    else:
        reprobado += 1
    suma = suma + calificacion
    if calificacion < baja:
        baja = calificacion
    else:
        alta = calificacion
promedio = suma / numero
print(f'Materias aprobadas: {aprobado}, materias reprobadas: {reprobado}')
print(f'Promedio de las calificaciones: {promedio}')
print(f'Calificación alta: {alta}, calificación baja: {baja}')