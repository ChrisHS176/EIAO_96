#1
import random
#2
def lanzar():
    #3
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    suma = d1 + d2
    #4
    print("---------------")
    print(f'Dado 1: {d1}')
    print(f'Dado 2: {d2}')
    print(f'Suma: {suma}')
    #5
    return suma