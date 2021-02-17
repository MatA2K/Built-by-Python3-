from time import sleep
def contador(inicio, fim , passo):
        if passo < 0:
            passo *= -1
        if passo == 0:
            print("!!O valor zero é inválido, foi convertido para 1!!")
            passo = 1
        if inicio < fim:
            cont = inicio
            print(f"Contando de {inicio} até {fim} pulo {passo}:")
            while cont <= fim:
                print(f"{cont}", end=" ")
                sleep(0.3)
                cont += passo
            print(".. acabou")
            print("-"*30)
        else:
            print(f"Contando de {inicio} até {fim} pulo {passo}:")
            cont = inicio
            while cont >= fim:
                print(f"{cont}", end=" ")
                sleep(0.3)
                cont -= passo
            print(".. acabou")
            print("-"*30)
#Principal
contador(1, 10 , 1)
contador(10, 0, 2)
print("Sua vez de escolher a contagem ")
i = int(input("Defina INICIO: "))
f = int(input("Defina o FIM: "))
p = int(input("Defina o PASSO(PULO): "))
contador(i, f, p)