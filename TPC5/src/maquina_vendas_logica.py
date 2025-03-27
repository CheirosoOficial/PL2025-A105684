import leitor_json
import re

### Metodos logicos
def carregar_maquina():
    list_stock = leitor_json.parse_json_stock("test.json")
    return list_stock

def listar_maquina(list_stock):
    print(  "maq:" +
            "\n cod | nome | quantidade | preço" +
            "\n---------------------------------")
    for key in list(list_stock.keys()):
        nome, quantidade, preco = list_stock[key]
        print(f" {key} | {nome} | {quantidade} | {preco} ")
    return

def print_saldo(total_coins):
    euros = total_coins // 100
    cents = total_coins % 100
    print(f"maq: Saldo = {euros}e{cents}c")

def adicionar_maquina(total_coins, value):
    total_coins += value
    print_saldo(total_coins)
    return total_coins

def selecionar_maquina(machine, codigo):
    _, total_coins, list_stock = machine
    if codigo in list_stock:
        nome, quantidade, preco = list_stock[codigo]
        preco = preco * 100
        if quantidade > 0 and preco <= total_coins:
            quantidade -= 1; total_coins -= int(preco); list_stock[codigo] = (nome, quantidade, preco/100)
            print(f"maq: Pode retirar o produto dispensado \"{nome}\"")
            print_saldo(total_coins)
        elif quantidade == 0:
            print("maq: Quantidade insufuciente para satisfazer o seu pedido")
            print_saldo(total_coins)
        else:
            print("maq: Saldo insufuciente para satisfazer o seu pedido")
            print_saldo(total_coins)
    resultado = total_coins, list_stock
    return resultado

def logica_maquina(machine, token):
    current_state, total_coins, list_stock = machine
    match current_state:
        case "LISTAR":
            listar_maquina(list_stock)
        case "SELECIONAR":
            if re.match(r"[A-Z]\d+", token):
                total_coins, list_stock = selecionar_maquina(machine, token)
        case "MOEDA":
            if type(token) is int:
                total_coins = adicionar_maquina(total_coins, token)
        case "SAIR":
            exit()
    machine = (current_state, total_coins, list_stock)
    return machine

