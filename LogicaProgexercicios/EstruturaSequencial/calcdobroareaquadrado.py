#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

Lado = float(input('Digite o lado do quadrado: ')) 
area = Lado ** 2
dobro = area * 2
print(f'O dobro da área do quadrado é {format(dobro, ".2f")}')
