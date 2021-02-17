def area(l, c):
    m = l * c
    print(f"A área de um terreno {l}x{c} é de {m}m²")

#Principal
print("Controle de Terreno")
print("-"*20)
lar = float(input("Largura (m): "))
com = float(input("Comprimento (m): "))
area(l=lar, c=com)