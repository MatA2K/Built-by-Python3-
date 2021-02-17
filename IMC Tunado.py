from time import sleep
dic = {}
dic['IMC'] = ( "Abaixo de 18.5 ", "Entre 18.5 e 24.9 ", "Entre 25 e 29.9 ",
              "Entre 30 e 39.9 ", "Acima de 40 ")
dic['Classe'] = ("| MAGREZA",
                 "| NORMAL",
                 "| SOBREPESO",
                 "| OBESIDADE",
                 "| OBESIDADE GRAVE")
dic['Grau'] = ("0", "0", "1", "2", "3")
def l():
    print("-"*40)
l()
print("\033[7;38mAnálise IMC (Índice de Massa Corporal)\033[m")
l()
peso = float(input("Peso(kg): "))
altura = float(input("Altura(m): "))
print(f"Foram informados {peso}kg e {altura}m")
l()
print("Analisando seu Indíce de massa corporal...")
sleep(2)
imc = peso / (altura * altura)
print(f"\033[7;38mSeu IMC é de {imc:.2f}\033[m")
l()
print("Atencão aos detalhes desse valor: ")
if imc <= 18.5:
    print("Obesidade grau 0 - \033[42m MAGREZA \033[m")
elif 18.5 < imc <= 24.9:
    print("Obesidade grau 0 - \033[44m NORMAL \033[m")
elif 25 <= imc <= 29.9:
    print("Obesidade grau 1 - \033[45m SOBREPESO \033[m")
elif 30 <= imc <= 39.9:
    print("Obesidade grau 2 - \033[43m OBESIDADE \033[m")
elif imc > 40:
    print("Obesidade grau 3 - \033[41m OBESIDADE GRAVE \033[m")