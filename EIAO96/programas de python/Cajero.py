saldo = 1000
while True:
    print("Elija que desea hacer")
    print("1. Consultar Saldo")
    print("2. Depositar")
    print("3. Retirar dinero")
    print("4. Salir")
    respuesta = input()
    respuesta = int(respuesta)
    if respuesta == 1:
        print("Tu saldo es: $", saldo)
    elif respuesta == 2:
        deposito = input("¿Cúanto desea depositar?: ")
        deposito = int(deposito)
        if deposito > 0:
            saldo = saldo + deposito
            print("Tu saldo es: $", saldo)
        else:
            print("No puede ingresar esa cantidad")
    elif respuesta == 3:
        retiro = input("¿Cúanto desea retirar?")
        retiro = int(retiro)
        if retiro > saldo:
            print("Saldo insuficiente")
        elif retiro <= 0:
            print("Ingrese una opción valida")
        else:
            saldo = saldo - retiro
            print("Tu saldo es: $", saldo)
    elif respuesta == 4:
        break
    else:
        print("Ingrese una opción valida")