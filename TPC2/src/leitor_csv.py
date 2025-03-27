import re
import json

# Abrir ficheiro
def open_file(file_name):
    f = open(file_name, 'r', encoding='utf-8')
    message = f.read()
    f.close()
    return message

# Normalizar os tabs que aparecem no inicio da descrição
def normalizar_csv(message):
    removing_tabs = re.sub(r'\n {9}', ' ', message, 0, re.MULTILINE)
    list_lines = re.split(r'\n', removing_tabs)
    if not list_lines: return {}
    else: return list_lines

# Converter o csv em um dictionario
def convert_csv_to_list(csv_file):
    message = open_file(csv_file)
    list_lines = normalizar_csv(message)

    category_names = list_lines[0].split(";")
    map_category = {cat: [] for cat in category_names}

    for line in list_lines[1:]:
        line_separated = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
        for i, cat in enumerate(category_names):
            if i < len(line_separated):
                map_category[cat].append(line_separated[i])

    return map_category



# Alinea A) Lista ordenada alfabeticamente dos compositores musicais
def list_alfabetic(map_csv):
    if "compositor" not in map_csv:
        return map_csv

    compositores = set(map_csv["compositor"])
    return sorted(compositores)

# Alinea B) Distribuição das obras por período: quantas obras catalogadas em cada período
def period_pieces(map_csv):
    period = map_csv.get("periodo", [])
    period_count = {}
    for p in period:
        period_count[p] = period_count.get(p, 0) + 1  # Conta ocorrências
    return period_count

# Alinea C) Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período
def period_pieces_dict(map):
    period = map.get("periodo", [])
    titles = map.get("nome", [])

    period_dict = {}

    for p, t in zip(period, titles):
        period_dict.setdefault(p, []).append(t)

    for p in period_dict:
        period_dict[p].sort()

    return period_dict



# Imprimir Resultados
csv_data = convert_csv_to_list("teste_3.csv")
print("Resultado da Leitura:")
print(json.dumps(csv_data, indent=2, ensure_ascii=False))

print("\n\nResultado das Queries:")
print(list_alfabetic(csv_data))
print(period_pieces(csv_data))
print(json.dumps(period_pieces_dict(csv_data), indent=2, ensure_ascii=False))