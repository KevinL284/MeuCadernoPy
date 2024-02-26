import random

class Carta:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor

def gerar_cartas(n):
    numeros = [random.randint(1, 10) for _ in range(n)]
    cores = [random.choice(['azul', 'preto', 'vermelho']) for _ in range(n)]
    return [Carta(num, cor) for num, cor in zip(numeros, cores)]

def jogar():
    n = int(input("Você deseja adivinhar um conjunto de 5 ou 10 cartas? "))
    cartas = gerar_cartas(n)
    pontuacao = 0

    while cartas:
        palpite_num = int(input("Adivinhe o número da carta (entre 1 e 10): "))
        palpite_cor = input("Adivinhe a cor da carta (azul, preto, vermelho): ")

        for i, carta in enumerate(cartas):
            if carta.numero == palpite_num and carta.cor == palpite_cor:
                del cartas[i]
                pontuacao += 5
                print("Acertou! Sua pontuação é agora", pontuacao)
                break
        else:
            pontuacao -= 1
            print("Errou! Sua pontuação é agora", pontuacao)

        if input("Deseja continuar jogando? (s/n) ") == 'n':
            break

    print("Jogo encerrado. Sua pontuação final é", pontuacao)

jogar()
