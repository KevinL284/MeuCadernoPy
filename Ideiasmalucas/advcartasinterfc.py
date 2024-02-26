import random
import tkinter as tk
from tkinter import messagebox

class Carta:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor

def gerar_cartas(n):
    numeros = [random.randint(1, 10) for _ in range(n)]
    cores = [random.choice(['azul', 'preto', 'vermelho']) for _ in range(n)]
    return [Carta(num, cor) for num, cor in zip(numeros, cores)]

def verificar_palpite():
    palpite_num = int(num_entry.get())
    palpite_cor = cor_entry.get().lower()

    global pontuacao

    for i, carta in enumerate(cartas):
        if carta.numero == palpite_num and carta.cor == palpite_cor:
            del cartas[i]
            pontuacao += 5
            pontuacao_label.config(text="Pontuação: " + str(pontuacao))
            resultado_label.config(text="Acertou!", fg="green")
            break
    else:
        pontuacao -= 1
        pontuacao_label.config(text="Pontuação: " + str(pontuacao))
        resultado_label.config(text="Errou!", fg="red")

    if not cartas:
        messagebox.showinfo("Fim de Jogo", "Jogo encerrado. Sua pontuação final é " + str(pontuacao))
        root.destroy()

def iniciar_jogo():
    global cartas
    global pontuacao
    pontuacao = 0
    cartas = gerar_cartas(int(cartas_entry.get()))
    jogar_button.config(state=tk.NORMAL)
    iniciar_button.config(state=tk.DISABLED)
    cartas_entry.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Jogo de Cartas")

num_label = tk.Label(root, text="Número da Carta:")
num_label.pack()
num_entry = tk.Entry(root)
num_entry.pack()

cor_label = tk.Label(root, text="Cor da Carta:")
cor_label.pack()
cor_entry = tk.Entry(root)
cor_entry.pack()

jogar_button = tk.Button(root, text="Jogar", command=verificar_palpite, state=tk.DISABLED)
jogar_button.pack()

resultado_label = tk.Label(root, text="")
resultado_label.pack()

cartas_label = tk.Label(root, text="Quantidade de Cartas:")
cartas_label.pack()
cartas_entry = tk.Entry(root)
cartas_entry.pack()

iniciar_button = tk.Button(root, text="Iniciar Jogo", command=iniciar_jogo)
iniciar_button.pack()

pontuacao_label = tk.Label(root, text="Pontuação: 0")
pontuacao_label.pack()

root.mainloop()