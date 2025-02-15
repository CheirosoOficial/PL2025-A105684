import re


def open_file(file_name):
    f = open(file_name, 'r', encoding='utf-8')
    message = f.read()
    f.close()
    return message


def convert_csv_to_list(csv_file):
    message, i = open_file(csv_file), 1

    list_lines = re.split(r'\n[^\s]', message.strip())
    if not list_lines: return {}

    category_names = re.split(r';', list_lines[0])
    map_category = {cat: [] for cat in category_names}

    for line in list_lines[1:]:
        values = re.split(r';', line)
        for i, value in enumerate(values):
            if i < len(category_names):
                map_category[category_names[i]].append(value)

    return map_category


    # Alinea A) Lista ordenada alfabeticamente dos compositores musicais
def list_alfabetic(map):
    if "compositor" not in csv_data:
        print("A categoria 'Compositor' não foi encontrada no CSV.")
        return csv_data

    compositores = csv_data["compositor"]

    dados_ordenados = sorted(zip(*csv_data.values()), key=lambda x: x[1])  # Índice 1 = "Compositor"

    csv_data_ordenado = {chave: [] for chave in csv_data}
    for linha in dados_ordenados:
        for chave, valor in zip(csv_data.keys(), linha):
            csv_data_ordenado[chave].append(valor)

    return csv_data_ordenado


     # Alinea B) Distribuição das obras por período: quantas obras catalogadas em cada período
def period_pieces(map, period):
    return list


    # Alinea C) Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período
def dictionary_period_pieces(map):
    return map




csv_data = convert_csv_to_list("obras.csv")

csv_data = list_alfabetic(csv_data)
compositores = csv_data["compositor"]
primeiros_elementos = {categoria: valores[0] for categoria, valores in csv_data.items() if valores}
print(compositores)