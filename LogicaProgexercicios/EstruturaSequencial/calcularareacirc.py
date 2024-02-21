#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

while True: 
    try:
        raio = float(input('Digite o raio do círculo:'))
        break
    except ValueError:
        print('O valor informado não é um número válido.')
    
area = 3.14 * (raio ** 2)
    
print(f"A área do círculo é {format(area, '.2f')}")

