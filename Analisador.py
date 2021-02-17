media = 0
totmedia = 0
velho = 0
nomevelho = 0
mulheres = 0
print("===== ANALISADOR DE COBAIAS =====")
for p in range (1, 5):
    nome = str(input("Nome da {}º pessoa: ".format(p)))
    idade = int(input("Idade da {}º pessoa: ".format(p)))
    sexo = str(input("Genêro da {}º pessoa, [M/F]: ".format(p))).upper()
    if sexo == "F":
        if idade < 20:
            mulheres += 1
    if p == 1 and sexo == "M":
        velho = idade
        nomevelho = nome
    if sexo in "Mn" and idade > velho:
        velho = idade
        nomevelho = nome
    media += idade
totmedia = media / 4

print("O total de mulheres com menos de 20 anos é {}".format(mulheres))
print("A média de idade do grupo é {:.0f} anos".format(totmedia))
print("O Homem mais velho é o {} com {} anos".format(nomevelho, velho))
