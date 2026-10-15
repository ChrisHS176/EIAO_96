#6
from dados import lanzar
#7
print("Lanzando dados...")
#8
s1 = lanzar()
#9
if s1 == 7 or s1 == 11:
    print("¡GANASTE!")
    print("---------------")
#10
elif s1 == 2 or s1 == 3 or s1 == 12:
    print("PERDISTE")
    print("---------------")
#11
else:
    print("No ganaste ni perdiste todavía")
    print("---------------")
    print("Tienes una segunda oportunidad")
    print(f'Tu suma objetiva es: {s1}')
    print(f'si sale 7 pierdes, si sale {s1} ganas')
    print("---------------")
    s2 = 0
    while s1 != s2 and s2 != 7:
        print("Lanzando dados nuevamente...")
        #12
        s2 = lanzar()
        if s1 == s2:
            print("¡GANASTE!")
            print("---------------")
        elif s2 == 7:
            print("PERDISTE")
            print("---------------")
        else:
            print("Intentando otra vez...")
            print("---------------")