from random import randint
print("==========  JOGO DA ADIVINHAÇÃO ===========")
print("Tente adivinhar o número que a máquina pensou...")
print("="*50)
jog = int(input("De 0 a 20, em qual número a CPU pensou? "))
CPU = randint(0, 20)
tentativas = 0
while jog != CPU:
    if jog < CPU:
        print("Mais..")
    elif jog > CPU:
        print("Menos...")
    jog = int(input("====== Tente de novo: ".format(CPU)))
    tentativas += 1
print("-------- Acertou com {} tentativas ---------!!".format(tentativas))
if tentativas > 4:
    print("CPU - 'HAHAHA, QUE FIASCO'")