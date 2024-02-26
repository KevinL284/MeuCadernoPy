# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

Metros_quadrados = float(input('Digite o tamanho em metros quadrados da área a ser pintada: '))
Litros = Metros_quadrados / 3
Latas = Litros / 18
Preco = Latas * 80

print(f'Você precisará de {Latas:.0f} latas de tinta e o preço total será de R${Preco:.2f}')