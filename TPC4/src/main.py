import ply.lex as lex

# Lista de tokens
tokens = (
    'KEYWORD',
    'VARIABLE',
    'IDENTIFIER',
    'STRING',
    'NUMBER',
    'SYMBOL'
)

# Expressões regulares para os tokens
t_ignore = ' \t'

# Simbolos da Linguagem
t_SYMBOL = r'[{}.@:]'

# Palavras-chave da Linguagem
keywords = {'select', 'where', 'limit', 'a'}

def t_KEYWORD(t):
    r'[a-zA-Z]+'
    if t.value.lower() in keywords:
        t.value = t.value.lower()
        return t
    else:
        t.type = 'IDENTIFIER'
        return t

def t_VARIABLE(t):
    r'\?[a-zA-Z0-9_]+'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z]+:[a-zA-Z0-9_]+'
    return t

def t_STRING(t):
    r'\"[^\"]*\"(@[a-zA-Z]+)?'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Criar o analisador léxico
lexer = lex.lex()

def analyze_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    lexer.input(data)
    tokens_dict = {
        "KEYWORD": [],
        "VARIABLE": [],
        "IDENTIFIER": [],
        "STRING": [],
        "NUMBER": [],
        "SYMBOL": []
    }

    for tok in lexer:
        tokens_dict[tok.type].append(tok.value)

    return tokens_dict


# Executando o metodo
result = analyze_file("./test.txt")
print(result)


