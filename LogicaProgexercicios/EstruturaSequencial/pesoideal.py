#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

def calcular_peso_ideal(altura, genero):
    if genero.lower() == 'homem':
        return (72.7 * altura) - 58
    elif genero.lower() == 'mulher':
        return (62.1 * altura) - 44.7
    else:
        return None

altura = float(input("Digite sua altura em metros: "))
genero = input("Você é homem ou mulher? ")
peso_ideal = calcular_peso_ideal(altura, genero)

if peso_ideal is not None:
    print(f"Seu peso ideal é {format(peso_ideal, '.2f')} kg.")
else:
    print("Por favor, insira 'homem' ou 'mulher' para o gênero.")



