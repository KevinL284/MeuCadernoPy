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
    # Tokens adicionais para C
    'C_KEYWORD': r'(int|float|char|void|if|else|for|while|do|switch|case|break|continue|return)',
    'C_OPERATOR': r'(&&|\|\||==|!=|<=|>=|<|>|=|\+|-|\*|/|%|!)',
    # Tokens adicionais para Java
    'JAVA_KEYWORD': r'(int|float|char|void|if|else|for|while|do|switch|case|break|continue|return|public|private|protected|static|final|class)',
    'JAVA_OPERATOR': r'(&&|\|\||==|!=|<=|>=|<|>|=|\+|-|\*|/|%|!)',
    # Tokens adicionais para Python
    'PYTHON_KEYWORD': r'(if|else|elif|while|for|in|def|return|True|False|None)',
    'PYTHON_OPERATOR': r'(&&|\|\||==|!=|<=|>=|<|>|=|\+|-|\*|/|%|!)',
}

def validar_token(token):
    for tipo, padrao in tokens.items():
        if re.fullmatch(padrao, token):
            return tipo
    return 'INVÁLIDO'

def verificar_tokens():
    entrada = entrada_text.get("1.0", tk.END).strip()
    tokens_digitados = entrada.split()
    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, f"Total de tokens digitados: {len(tokens_digitados)}\n\n")
    for token in tokens_digitados:
        tipo = validar_token(token)
        resultado_text.insert(tk.END, f"Token: {token}\nTipo: {tipo}\nValidade: {'Válido' if tipo != 'INVÁLIDO' else 'Inválido'}\n\n")

# Criando a janela principal
janela = tk.Tk()
janela.title("Analisador Léxico")
janela.geometry("400x400")

# Criando o campo de entrada
entrada_label = tk.Label(janela, text="Digite os tokens:")
entrada_label.pack()

entrada_text = tk.Text(janela, height=5)
entrada_text.pack()

# Criando o botão de verificação
verificar_button = tk.Button(janela, text="Verificar Tokens", command=verificar_tokens)
verificar_button.pack()

# Criando o campo de resultado
resultado_label = tk.Label(janela, text="Resultado:")
resultado_label.pack()

resultado_text = tk.Text(janela, height=15)
resultado_text.pack()

# Iniciando a interface
janela.mainloop()
