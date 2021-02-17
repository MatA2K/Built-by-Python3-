from time import sleep
ficha = []
print("=" * 25)
print("CONSULTA BOLETIM ESCOLAR")
print("=" * 25)
while True:
    nome = str(input("Nome: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input("Quer continuar?[S/N]: ")).upper()
    print("-"*25)
    if resp == "N":
        break
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print("."*25)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print("."*25)
while True:
    opc = int(input("Quer saber a nota de qual aluno? [999 para encerrar]: "))
    if opc == 999:
        print("Encerrando...")
        sleep(2)
        break
    sleep(2)
    if opc <= len(ficha)-1:
        print((f"As Notas do {ficha[opc][0]} foram {ficha[opc][1]}"))
        print("-"*35)