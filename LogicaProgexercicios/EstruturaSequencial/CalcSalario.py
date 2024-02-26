# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

GanhoHora = float(input('Quanto você ganha por hora? '))
HorasTrabalhadasMes = float(input('Quantas horas você trabalha por mês? '))

GanhoTotal = GanhoHora * HorasTrabalhadasMes
print(f"Seu salário total é R${format(GanhoTotal, '.2f')}")