import re
import tkinter as tk

# Definindo os tokens
tokens = {
     # Palavra-chave (keywords)
    'C_KEYWORD': r'\b(int|float|char|void|if|else|for|while|do|switch|case|break|continue|return)\b',
    'JAVA_KEYWORD': r'\b(int|float|char|void|if|else|for|while|do|switch|case|break|continue|return|public|private|protected|static|final|class)\b',
    'PYTHON_KEYWORD': r'\b(if|else|elif|while|for|in|def|return|True|False|None)\b',

    # Número (inteiros e floats)
    'FLOAT': r'\d*\.\d+',
    'INT': r'\b\d+\b',

    # Identificador
    'ID': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',

    # String
    'STRING': r'"([^"\\]*(\\.[^"\\]*)*)"',  # Strings entre aspas duplas
    'CHAR': r"\'([^'\\]*(\\.[^'\\]*)*)\'",  # Caracteres entre aspas simples

    # Delimitador
    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'LBRACE': r'\{',
    'RBRACE': r'\}',
    'LBRACKET': r'\[',
    'RBRACKET': r'\]',
    'COMMA': r',',
    'SEMICOLON': r';',

    # Operador
    'C_OPERATOR': r'(&&|\|\||==|!=|<=|>=|<|>|=|\+|-|\*|/|%|!)',
    'JAVA_OPERATOR': r'(&&|\|\||==|!=|<=|>=|<|>|=|\+|-|\*|/|%|!)',
    'PYTHON_OPERATOR': r'(and|or|==|!=|<=|>=|<|>|=|\+|-|\*|/|%|!)',

    # Espaços em branco
    'WHITESPACE': r'\s+',

    # Desconhecido
    'UNKNOWN': r'.',  # Qualquer outro caractere
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
