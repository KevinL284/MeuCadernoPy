import re
import tkinter as tk

# Definindo os tokens
tokens = {
    'INT': r'\d+',
    'FLOAT': r'\d*\.?\d+',
    'ID': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'PLUS': r'\+',
    'MINUS': r'-',
    'MULTIPLY': r'\*',
    'DIVIDE': r'/',
    'LPAREN': r'\(',
    'RPAREN': r'\)',
}

# Função para analisar o código fonte
def lex(code):
    # Lista para armazenar os tokens encontrados
    token_list = []

    # Iterar sobre o código fonte
    while code:
        # Remover espaços em branco no início do código
        code = code.strip()

        # Verificar se o código corresponde a algum token
        for token_name, token_pattern in tokens.items():
            match = re.match(token_pattern, code)
            if match:
                # Adicionar o token encontrado à lista
                token_value = match.group(0)
                token_list.append((token_name, token_value))
                # Atualizar o código removendo o token encontrado
                code = code[len(token_value):]
                break
        else:
            # Se nenhum token corresponder, gerar um erro
            raise ValueError(f"Invalid token: {code}")

    return token_list

# Função para processar o código inserido pelo usuário
def process_code():
    user_input = code_entry.get()
    try:
        tokens = lex(user_input)

        count = 0
        token_types = set()

        for token in tokens:
            count += 1
            token_types.add(token[0])

        result_label.config(text=f"Total tokens: {count}\nToken types: {', '.join(token_types)}")
        error_label.config(text="")
    except ValueError as e:
        result_label.config(text="")
        error_label.config(text=str(e))

# Criar a janela principal
window = tk.Tk()
window.title("Analisador Léxico")
window.geometry("400x250")

# Criar os widgets
code_label = tk.Label(window, text="Enter the code:")
code_label.pack()

code_entry = tk.Entry(window, width=50)
code_entry.pack()

process_button = tk.Button(window, text="Process", command=process_code)
process_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

error_label = tk.Label(window, text="", fg="red")
error_label.pack()

# Iniciar o loop principal da janela
window.mainloop()
