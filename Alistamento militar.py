from datetime import date
print("  ALISTAMENTO MILITAR  ")
nome = str(input("Qual o seu nome jovem? "))
idade = int(input("Qual seu ano de nascimento jovem? "))
ano = date.today().year
alist = ano - idade
S = 18 - alist
N = alist - 18
if alist == 18:
    print("Está na hora de se alistar, vou preparar tudo..")
elif alist < 18:
    print("Faltam {} ano(s) para o alistamento".format(S))
elif alist > 18:
    print("Já devia ter se alistado a {} ano(s)".format(N))
    print("Vai ter que trazer justificativa, senão, procura seus direitos")

