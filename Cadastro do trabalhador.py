from datetime import date
dicio = dict()
dicio['Nome'] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
dicio['Idade'] = date.today().year - nasc
carteira = int(input("Carteira de trabalho (0 se não tiver): "))
if carteira != 0:
    dicio['contrato'] = int(input("Ano de contratação: "))
    dicio['salario'] = float(input("Salário: R$"))
    dicio['aposenta'] = dicio['Idade'] + dicio['contrato']+35 - date.today().year
    for k,v in dicio.items():
        print(f" - {k} tem o valor {v}")
else:
    for k,v in dicio.items():
        print(f" - {k} tem o valor {v}")
    print(" - Não possui CTPS")