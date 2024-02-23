#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A: O produto do dobro do primeiro com metade do segundo .
# B: A soma do triplo do primeiro com o terceiro.
# C: O terceiro elevado ao cubo.

def input_numero(tipo):
    while True: 
        try:
            if tipo == 'inteiro':
                numero = int(input('Digite um número inteiro: '))
            else:
                numero = float(input('Digite um número real: '))
            return numero
        except ValueError:
            print('O valor informado não é um número válido, por favor digite outro númeor válido. ')
            
num1 = input_numero('inteiro')
num2 = input_numero('inteiro')
num3 = input_numero('real')

resposta_A = (num1 * 2) * (num2 / 2)
resposta_B = (num1 * 3) + num3
resposta_C = num3 ** 3

print(f'A: O produto do dobro do primeiro com metade do segundo é {resposta_A}')
print(f'B: A soma do triplo do primeiro com o terceiro é {resposta_B}')
print(f'C: O terceiro elevado ao cubo é {resposta_C}') 
