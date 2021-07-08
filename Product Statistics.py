print("="*30)
print("  LOJA REI DOS DISPOSITIVOS  ")
print("="*30)
tot = vMil = menor = cont = 0
barato = ""
while True:
    nome = str(input("Digite o nome do produto: "))
    valor = float(input("Digite o preço do produto: R$"))
    cont = 1
    print("_"*34)
    seguir = " "

    if valor > 1000: #Valor maior que 1000
        vMil += 1

    tot += valor #Total gasto

    if cont == 1 or valor < menor: #Produto mais barato
        menor = valor
        barato = nome

    while seguir not in "SN":
        seguir = str(input("Quer continuar [S/N]? ")).upper()[0].strip()
    if seguir == "N":
        break
print("======    Obrigado pela compra     ======")
print(f"No total, {vMil} produto(s) custa(m) mais que R$1.000")
print(f"O nome do produto mais barato é {barato}")
print(f"O total gasto na compra foi R${tot:.2f}")
print("======        Volte Sempre         ======")
