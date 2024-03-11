#Faça um Programa que leia três números e mostre-os em ordem decrescente.

def obter_valor():
    while True: 
        try:
            valor = int(input("Informe um número: "))
            break
        except ValueError:
            print("O valor informado não é um número válido, por favor digite um número válido.")
    return valor

num1 = obter_valor()
num2 = obter_valor()
num3 = obter_valor()

if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else:
    if num1 <= num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)