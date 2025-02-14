import re


def open_file(file_name):
    f = open(file_name, 'r', encoding='utf-8')
    message = f.read()
    f.close()
    return message

def convert_csv_to_list(csv_file):
    message, i = open_file(csv_file), 1

    list_lines = re.split('\n', message)
    category_names = re.split(';', list_lines[0])

    # map_category = {
    #     for cat in category_names:
    #         [cat, ]
    # }

    while i < len(list_lines):
        list_categories = re.split(';', list_lines[i])

    return list_categories

def list_alfabetic(list):
    return list


def period_pieces(list):
    return list

def dictionary_period_pieces(list):
    return list


print(convert_csv_to_list("obras.csv"))