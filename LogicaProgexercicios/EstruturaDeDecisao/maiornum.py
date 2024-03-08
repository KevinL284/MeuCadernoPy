# Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else: num1 == num2
print("Os números são iguais")