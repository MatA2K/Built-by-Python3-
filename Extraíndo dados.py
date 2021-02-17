lista = []
while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    seguir = str(input("Quer continuar [S/N]? ")).upper()[0].strip()
    print("-"*25)
    if seguir == "N":
        break
print("-="*16)
print(f"Foram digitados {len(lista)} valores")
print("="*26)
lista.sort(reverse=True)
print(f"A lista decrescente: {lista}")
print("="*33)
if 5 in lista:
    print(f"O valor 5 está lista!")
else:
    print("O valor 5 não foi listado..")