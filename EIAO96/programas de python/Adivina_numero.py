import random
print("Adivina el número")
contador = 1
pregunta = input("Elige un número del 1 al 100: ")
pregunta = int(pregunta)
numero = random.randint(1,100)
while not pregunta == numero:
    if pregunta < numero:
        pregunta = input("El número es más alto, vuelve a intentar:")
    else:
        pregunta = input("El número es más pequeño, vuelve a intentar: ")
    pregunta = int(pregunta)
    contador = contador + 1
if contador == 1:
    print("No puedo creerlo! Acertaste a la primera")
else:
    print("Adivinaste el número en ", contador, " intentos")