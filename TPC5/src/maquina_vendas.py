import ply.lex as lex
import re
import machine as mac


### Tokens e estados do meu alfabeto
tokens = ["COMMAND", "COINS", "CODES"]
states = [("LISTAR", "exclusive"), ("SELECIONAR", "exclusive"), ("MOEDA", "exclusive"), ("SAIR", "exclusive")]


### Metodos para a construção do lexer
# Characteres a serem ignorados pelo lexer
t_ANY_ignore = " "
t_SELECIONAR_CODES = r"[A-Z]\d+"

# Comando para adicionar moedas
def t_MOEDA_COINS(t):
    r"\d+[ec]"
    match = re.match(r"(\d+)([ec])", t.value)
    if match:
        valor, tipo = match.groups()
        t.value = int(valor) * 100 if tipo == "e" else int(valor)
    return t

def t_ANY_COMMAND(t):
    r"^([A-Z]+)"
    match t.value:
        case "LISTAR":
            t.lexer.begin("LISTAR")
        case "MOEDA":
            t.lexer.begin("MOEDA")
        case "SELECIONAR":
            t.lexer.begin("SELECIONAR")
        case "SAIR":
            t.lexer.begin("SAIR")
        case _:
            return t
    return t

def t_ANY_error(t):
    print(f"maq: erro operação Invalida - {t.value[0]}")
    t.lexer.skip(1)

### Construindo o lexer a partir das regras anteriormente definidas
lexer = lex.lex()


### Função main
def main():
    print(  "maq: 2024-03-08, Stock carregado, Estado atualizado." +
            "\nmaq: Bom dia. Estou disponível para atender o seu pedido.")

    total_coins = 0
    list_stock = mac.carregar_maquina()
    while True:
        prompt = input(">> ")
        lexer.input(prompt)
        while token := lexer.token():
            machine = (lexer.current_state(), total_coins, list_stock)
            _, total_coins, list_stock = mac.logica_maquina(machine, token.value)
        lexer.begin("INITIAL")

if __name__ == "__main__":
    main()