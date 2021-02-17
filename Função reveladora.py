from time import sleep
def maior(* valores):
    cont = maior = 0
    print("\nAnalisando valores..")
    for valor in valores:
        print(f"{valor} ", end="")
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
            cont += 1
    print(f"O maior valor foi {maior}")

#Principal
maior(4, 7, 15, 20, 23)
maior(1, 5, 8, 16, 22)
maior(24, 52, 36, 10)