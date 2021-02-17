def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, NameError):
            print("ERRO, digite um valor inteiro")
            continue
        else:
            return n


def leiaFloat(num):
    while True:
        try:
            n = float(input(num))
        except (ValueError, NameError):
            print("\033[31mERRO, Digite um valor real\033[m")
            continue
        else:
            return n

n1 = leiaInt("Digite um valor inteiro: ")
n2 = leiaFloat("Digite um valor real: ")
print(f"O valor inteiro foi {n1} e o valor real foi {n2}")