# Descrição: Receba quatro notas de um aluno e calcule a média.
# E exiba uma mensagem de acordo com a média e o conceito.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print(f'Aprovado com média {media}')
elif media < 7 and media >= 5:
    print(f'Recuperacao com média {media}')
else:
    print(f'Reprovado com média {media}')