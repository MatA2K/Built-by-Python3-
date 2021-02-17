from datetime import date
print("CONFEDERAÇÃO MARCIAL DE NATAÇÃO")
nas = int(input("Qual seu ano de nascimento? "))
ano = date.today().year
idade = ano - nas
if idade <= 9:
    print("Você é da categoria MIRIM")
elif idade <=14:
    print("Você é da categoria INFANTIL")
elif idade <= 19:
    print("Você é da categoria JUNIOR")
elif idade <= 25:
    print("Você é da categoria SÊNIOR")
else:
    print("Você já é categoria MASTER")