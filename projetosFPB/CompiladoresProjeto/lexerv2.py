import re
import tkinter as tk
import sys
import io

# Definindo os tokens apenas para Python, categorizados
tokens = {
    'PALAVRA_CHAVE': r'\b(if|else|elif|while|for|in|def|return|True|False|None|print)\b',
    'IDENTIFICADOR': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'NUMERO': r'\b\d+\b|\d*\.\d+',
    'STRING': r'"([^"\\]*(\\.[^"\\]*)*)"|\'([^\'\\]*(\\.[^\'\\]*)*)\'',
    'DELIMITADOR': r'[\(\)\{\}\[\],;]',
    'OPERADOR': r'(and|or|==|!=|<=|>=|<|>|=|\+|-|\*|/|%|!)',
    'ESPACOS': r'\s+',
    'DESCONHECIDO': r'.',
}

def categorizar_tokens(codigo):
    # Dicionário para armazenar os tokens por categoria
    categorias = {
        'Palavra-chave': [],
        'Identificador': [],
        'Número': [],
        'String': [],
        'Delimitador': [],
        'Operador': [],
        'Espaços': [],
        'Desconhecido': [],
    }
    
    # Mantendo as strings intactas durante a análise
    tokens_digitados = re.findall(tokens['STRING'] + r'|\S+', codigo)
    
    for token in tokens_digitados:
        token_str = token[0] if isinstance(token, tuple) else token  # Tratar como string
        if re.fullmatch(tokens['PALAVRA_CHAVE'], token_str):
            categorias['Palavra-chave'].append(token_str)
        elif re.fullmatch(tokens['IDENTIFICADOR'], token_str):
            categorias['Identificador'].append(token_str)
        elif re.fullmatch(tokens['NUMERO'], token_str):
            categorias['Número'].append(token_str)
        elif re.fullmatch(tokens['STRING'], token_str):
            categorias['String'].append(token_str)
        elif re.fullmatch(tokens['DELIMITADOR'], token_str):
            categorias['Delimitador'].append(token_str)
        elif re.fullmatch(tokens['OPERADOR'], token_str):
            categorias['Operador'].append(token_str)
        elif re.fullmatch(tokens['ESPACOS'], token_str):
            categorias['Espaços'].append(token_str)
        else:
            categorias['Desconhecido'].append(token_str)
    
    return categorias

def verificar_tokens():
    entrada = entrada_text.get("1.0", tk.END).strip()
    categorias = categorizar_tokens(entrada)
    
    total_tokens = sum(len(categorias[cat]) for cat in categorias)

    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, f"Total de tokens: {total_tokens}\n\n")

    for categoria, tokens_lista in categorias.items():
        resultado_text.insert(tk.END, f"{categoria}: {len(tokens_lista)}\n")
        resultado_text.insert(tk.END, f"Tokens: {', '.join(tokens_lista)}\n\n")

def executar_codigo():
    entrada = entrada_text.get("1.0", tk.END).strip()
    resultado_execucao.delete("1.0", tk.END)
    
    resultado_execucao.insert(tk.END, "Iniciando a execução do código...\n")
    
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = mystdout = io.StringIO()
    sys.stderr = mystderr = io.StringIO()
    try:
        exec(entrada, {})
        resultado_execucao.insert(tk.END, mystdout.getvalue())
        resultado_execucao.insert(tk.END, "\nExecução concluída com sucesso!\n")
    except Exception as e:
        resultado_execucao.insert(tk.END, f"Erro na execução do código Python:\n{e}\n")
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        resultado_execucao.insert(tk.END, mystderr.getvalue())

# Criando a janela principal
janela = tk.Tk()
janela.title("Analisador Léxico e Compilador")
janela.geometry("800x600")

# Criando o campo de entrada
entrada_label = tk.Label(janela, text="Digite o código:")
entrada_label.pack()

entrada_text = tk.Text(janela, height=10)
entrada_text.pack()

# Criando o botão de verificação
verificar_button = tk.Button(janela, text="Verificar Tokens", command=verificar_tokens)
verificar_button.pack()

# Criando o campo de resultado de análise de tokens
resultado_label = tk.Label(janela, text="Resultado da Análise Léxica:")
resultado_label.pack()

resultado_text = tk.Text(janela, height=10)
resultado_text.pack()

# Criando o botão para executar o código
executar_button = tk.Button(janela, text="Executar Código", command=executar_codigo)
executar_button.pack()

# Criando o campo de resultado da execução
resultado_execucao_label = tk.Label(janela, text="Resultado da Execução:")
resultado_execucao_label.pack()

resultado_execucao = tk.Text(janela, height=10)
resultado_execucao.pack()

janela.mainloop()
