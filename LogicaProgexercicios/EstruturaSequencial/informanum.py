#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numero = input('informe um número: ')
while not numero.isnumeric():
    print('O valor informado não é um número válido.')
    numero = input('informe um número válido: ')
print(f'O número informado foi {numero}')
