#Faça um Programa que peça dois números e imprima a soma.

numero1 = input('Digite um número: ')
numero2 = input('Digite outro número: ')

while not numero1.isnumeric() or not numero2.isnumeric():
    print('Os valores informados não são números válidos.')
    numero1 = input('Digite um número válido: ')
    numero2 = input('Digite outro número válido: ')
    
soma = int(numero1) + int(numero2)
print(f'A soma dos números é {soma}')