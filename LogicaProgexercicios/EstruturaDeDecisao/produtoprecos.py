#Faça um programa que pergunte o preço de três produtos
# e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

ProdutoA = float(input("Digite o preço do produto A: "))
ProdutoB = float(input("Digite o preço do produto B: "))
ProdutoC = float(input("Digite o preço do produto C: "))

def obter_valor():
    while True: 
        try:
            valor = float(input("Informe o valor do produto: "))
            break
        except ValueError:
            print("O valor informado não é um número válido, por favor digite um número válido.")
    return valor

menor_valor = obter_valor

if ProdutoA < ProdutoB and ProdutoA < ProdutoC:
    print(f"O produto A é o mais barato, com o valor de R${ProdutoA}")
elif ProdutoB < ProdutoA and ProdutoB < ProdutoC:
    print(f"O produto B é o mais barato, com o valor de R${ProdutoB}")
else:
    print(f"O produto C é o mais barato, com o valor de R${ProdutoC}")
    