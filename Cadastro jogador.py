print("-"*40)
print("----   Gerenciamento de carreira   ----")
print("-"*40)
dados = {}
lista = []
dados['Nome'] = str(input("Nome do jogador: "))
tot = int(input("Partidas disputadas: "))
for c in range(0, tot):
    lista.append(int(input(f"   Gols na partida {c}:  ")))
print("="*55)

dados['gols'] = lista.copy()
dados['total'] = sum(lista)
print(dados)
print("="*55)

for k,v in dados.items():
    print(f"O campo {k} tem o valor {v}")
print("="*55)

print(f"O jogador {dados['Nome']} disputou {tot} partidas:")
for i, v in enumerate(dados['gols']):
    print(f"   => Na partida {i+1}, fez {v}")
print(f"Foi um total de {dados['total']} gols.")