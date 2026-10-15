#1
import random
frases = ["Hola Mundo", "Qué tal", "¿Estás listo?", "Bienvenido" ,"Empieza ahora"]
print(random.choice(frases))
#2
cantidad = int(input("¿Cuántas personas deseas registrar?: "))
#3
if cantidad > 0:
    #4
    cantidadmenores = 0
    sumamenores = 0
    cantidadmayores = 0
    sumamayores = 0
    cantidad = cantidad + 1
    #5
    listanombres = []
    #6
    for i in range(1, cantidad):
        nombre = input(f'Ingresa el nombre de la persona {i}: ')
        edad = int(input(f'Ingresa la edad de {nombre}: '))
        #7
        listanombres.append(nombre)
        #8
        if edad > 0:
            #9
            if edad < 30:
                cantidadmenores = cantidadmenores + 1
                sumamenores = sumamenores + edad
            else:
                cantidadmayores = cantidadmayores + 1
                sumamayores = sumamayores + edad
        #10
        else:
            print("Edad no válida, ingresa una edad mayor a 0")
    #11
    if cantidadmenores > 0:
        promediomenores = sumamenores // cantidadmenores
    else:
        promediomenores = 0
    #12
    if cantidadmayores > 0:
        promediomayores = sumamayores // cantidadmayores
    else:
        promediomayores = 0
    #13
    print("========== Resultados ==========")
    print("Las personas que fueron registradas son: ", listanombres)
    print("Personas menores de 30 años: ", cantidadmenores)
    print("Promedio de edad de personas menores de 30 años: ", promediomenores)
    print("Personas mayores o iguales a 30 años: ", cantidadmayores)
    print("Promedio de edad de personas mayores o iguales a 30 años: ", promediomayores)
    print("================================")
#14
else:
    print("Cantidad no válida, ingresa un número mayor a 0")