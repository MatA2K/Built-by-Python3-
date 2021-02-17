from time import sleep
print("="*40)
print("   ANALISADOR DE DADOS PESSOAIS   ")
print("="*40)
contIdade = contM = contF = 0
seguir = ""

while True:
    idade = int(input("Qual a sua idade? "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Qual o seu sexo [M/F]? ")).upper()[0].strip()
    print("-"*35)
    print("Cadastro Efetuado")
    print("_"*35)

    if idade >= 18:
        contIdade += 1
    if sexo == "M":
        contM += 1
    if sexo == "F" and idade < 20:
        contF += 1
    seguir = " "
    while seguir not in "SN":
        seguir = str(input("Quer continuar [S/N]? ")).upper()[0].strip()
    if seguir == "N":
        break

print(f"Total de pessoas com mais de 18 anos: {contIdade}")
print(f"Total de Homens cadastrados: {contM}")
print(f"Total de mulheres com menos de 20 anos: {contF}")