def fatorial(num=1, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f"{c} ", end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" =  ", end='')
        f *= c
    return f


n = int(input("Digite um número para saber seu fatorial: "))
resp = str(input("Quer ver o cálculo fatorial? [S/N]: ")).upper()[0]
print("-"*40)
if resp == "S":
    print(fatorial(n, show=True))
elif resp == "N":
    print(fatorial(n, show=False))
