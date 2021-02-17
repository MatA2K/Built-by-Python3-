from time import sleep
num = int(input("Digite um número: "))
print("""Escolha uma base para conversão:
[ 1 ] Binario
[ 2 ] Hexadecimal
[ 3 ] Octal""")
op = int(input("Sua opção:"))
print("Aguarde..")
sleep(2)
if op == 1:
    print("A conversão para binário resultou em {}".format(bin(num)))
elif op == 2:
    print("A conversão para Hexadecimal resultou em {}".format(hex(num)))
elif op == 3:
    print("A conversão para octal resultou em {}".format(oct(num)))
else:
    print("Opção inválida!")