from TIME import SLEEP
print("-"*40)
print("----   Gerenciamento de carreira   ----")
print("-"*40)
dados = {}
lista = []
time = []
while True:
    dados.clear()
    dados['Nome'] = str(input("Nome do jogador: "))
    tot = int(input("Partidas disputadas: "))
    lista.clear()
    for c in range(0, tot):
        lista.append(int(input(f"   Gols na partida {c+1}:  ")))
    print("="*55)
    dados['gols'] = lista.copy()
    dados['total'] = sum(lista)
    time.append(dados.copy())
    while True:
        resp = str(input("Quer continuar? [S/N]: ")).upper()[0]
        if resp in "SN":
            break
        print("Inválido, tente novamente")
    if resp == "N":
        break
print("-"*50)
print("cod ", end="")
for i in dados.keys():
    print(f"{i:<17}", end="")
print()
print("-"*50)
for k,v in enumerate(time):
    print(f"{k:>2} ", end="")
    for dados in v.values():
        print(f"{str(dados):<18}", end="")
    print()
print("="*50)
while True:
    busca = int(input("Quer ver os dados de qual jogador? [999 para nenhum]: "))
    if busca == 999:
        break
    if busca > len(time):
        print("Inválido, esse jogador não está na lista")
    else:
        print(f"--- ANÁLISE DO {time[busca]['Nome'].upper()}: ---")
        for k,v in enumerate(time[busca]['gols']):
            print(f" No jogo {k}, ele marcou {v} gols")
    print("="*50)
print("Encerrando...")
sleep(2)
