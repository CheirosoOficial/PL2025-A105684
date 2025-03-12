import ply.lex as lex

# Define tokens
tokens = ('COD', 'NOME', 'QUANT', 'PRECO')

t_ignore = " \t\n"

# Regex patterns
def t_COD(t):
    r'"cod"\s*:\s*"(\w+)"'
    t.value = t.lexer.lexmatch.group(2)
    return t

def t_NOME(t):
    r'"nome"\s*:\s*"([^\"]+)"'
    t.value = t.lexer.lexmatch.group(4)
    return t

def t_QUANT(t):
    r'"quant"\s*:\s*(\d+)'
    t.value = int(t.lexer.lexmatch.group(6))
    return t

def t_PRECO(t):
    r'"preco"\s*:\s*([\d.]+)'
    t.value = float(t.lexer.lexmatch.group(8))
    return t

def t_error(t):
    t.lexer.skip(1)

# Inicializar o construtor
lexer = lex.lex()


def parse_json_stock(path):
    with open(path, "r", encoding="utf-8") as file:
        json_text = file.read()

    lexer.input(json_text)
    stock_map = {}
    current_item = {}

    while True:
        tok = lexer.token()
        if not tok:
            break

        if tok.type == 'COD':
            if current_item:
                stock_map[current_item['cod']] = (current_item['nome'], current_item['quant'], current_item['preco'])
            current_item = {'cod': tok.value}
        elif tok.type == 'NOME':
            current_item['nome'] = tok.value
        elif tok.type == 'QUANT':
            current_item['quant'] = tok.value
        elif tok.type == 'PRECO':
            current_item['preco'] = tok.value

    if current_item:
        stock_map[current_item['cod']] = (current_item['nome'], current_item['quant'], current_item['preco'])

    return stock_map