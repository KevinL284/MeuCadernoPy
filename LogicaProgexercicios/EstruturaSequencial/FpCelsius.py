#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

while True: 
    try:
         Fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))
         break
    except ValueError:
         print('O valor informado não é um número válido, por favor digite outro númeor válido. ')
Celcius = (Fahrenheit - 32) * 5/9
print(f"A temperatura em graus Celcius é {format(Celcius, '.2f')}")
