# Escreva um algoritmo que o usuário informe um número e o programa informe se o número é positivo, negativo ou zero.

def obter_numero():
    while True:
        try:
            numero = float(input("Informe um número: "))
            break
        except ValueError:
            print("O valor informado não é um número válido, por favor digite um número válido.")
    return numero

numero = obter_numero()

if numero > 0:
    print("O número informado é positivo.")
elif numero < 0:
    print("O número informado é negativo.")
elif numero == 0:
    print("O número zero é neutro.")
