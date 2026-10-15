import random
print("==========================")
print("Bienvenido al juego de Piedra, Papel o Tijera")
name = input ("Ingresa tu nombre: ")
print(f'{name} 0 vs. CPU 0')
print("==========================")
contador_usuario = 0
contador_cpu = 0
rondas = 0

while contador_usuario != 5 and contador_cpu != 5:
    ppo = input("Elige piedra, papel, tijera: ")
    ppo = ppo.lower()
    opcion = ["piedra", "papel", "tijera"]
    if ppo == "piedra" or ppo == "papel" or ppo == "tijera":
        cpu = random.choice(opcion)
        print(f'{name}: {ppo}, CPU: {cpu}')
        rondas += 1
        if cpu == ppo:
            print("Empate")
        elif (ppo == "piedra" and cpu == "tijera") or (ppo == "papel" and cpu == "piedra") or (ppo == "tijera" and cpu == "papel"):
            print(f"{name} gana")
            contador_usuario += 1
        else:
            print("CPU gana")
            contador_cpu += 1
        print(f'Contador: {name} {contador_usuario} - CPU {contador_cpu}')
        print("==========================")
    elif ppo == "salir":
        print("Juego terminado")
    else:
        print("Opción no permitida, intenta otra vez")
        print("==========================")

print(f'Rondas jugadas: {rondas}')
if contador_usuario == 5:
    print(f'¡Felicidades {name}! Has ganado el juego')
else:
    print(f'¡CPU ha ganado! Mejor suerte la próxima vez {name}')