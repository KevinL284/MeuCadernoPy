#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

while True: 
    try:
       Celcius = float(input('Digite a temperatura em graus Celcius: '))
       break
    except ValueError:
       print('O valor informado não é um número válido, por favor digite um número válido. ')
Fahrenheit = Celcius * 9/5 + 32
print(f"A temperatura em graus Fahrenheit é {format(Fahrenheit, '.2f')}")