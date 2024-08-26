# Definindo os tokens
import re


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

# Exemplo de uso
code = "3.14 + 2 * (4 - 1)"
tokens = lex(code)
for token in tokens:
    print(token)