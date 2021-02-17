def ficha(nome='<Null>', gols=0):
    print(f"O jogador {nome} marcou {gols} gols no campeonato")


n = str(input("Nome do jogador: "))
g = str(input("Gols marcados: "))
if g.isnumeric():
    g = int(g)
else:
    gols = 0
if n.strip() == " ":
    ficha(nome=g)
else:
    ficha(n, g)
