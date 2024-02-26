# Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# A: comprar apenas latas de 18 litros;
# B: comprar apenas galões de 3,6 litros;
# C: misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

def calcular_tinta(area):
    litros_necessarios = area / 6 * 1.1
    latas = math.ceil(litros_necessarios / 18)
    galoes = math.ceil(litros_necessarios / 3.6)
    misto_latas = math.floor(litros_necessarios / 18)
    misto_galoes = math.ceil((litros_necessarios - misto_latas * 18) / 3.6)
    return [(latas, latas * 80), (galoes, galoes * 25), (misto_latas, misto_galoes, misto_latas * 80 + misto_galoes * 25)]

area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
resultados = calcular_tinta(area)
print(f"A: {resultados[0][0]} latas de 18 litros. Preço: R$ {resultados[0][1]}")
print(f"B: {resultados[1][0]} galões de 3,6 litros. Preço: R$ {resultados[1][1]}")
print(f"C: {resultados[2][0]} latas e {resultados[2][1]} galões. Preço: R$ {resultados[2][2]}")
