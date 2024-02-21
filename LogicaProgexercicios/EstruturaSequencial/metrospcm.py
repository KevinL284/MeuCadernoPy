# Faça um Programa que converta metros para centímetros.
while True:
    try:
        metros = float(input('Digite a quantidade de metros: '))
        break
    except ValueError:
        print('O valor informado não é um número válido.')
centimetros = metros * 100
print(f"{metros} metros é igual à {format(centimetros, '.2f')} centímetros.")