from time import sleep
from random import randint

def sorteia(lista):
    print("Contando: ", end="")
    for c in range(0, 5):
        n = randint(1, 25)
        lista.append(n)
        print(f"{n}", end=" ")
        sleep(0.3)
    print(' .. acabou')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"A soma de todos os pares de {lista}, resulta em {soma}")

numeros = list()
sorteia(numeros)
somaPar(numeros)