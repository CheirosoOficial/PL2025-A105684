# Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
# Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
# Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
# Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

def sum_reader(string):
    on_off = True
    sum_total, i = 0, 0
    string = string.lower()

    while i < len(string):
        if string[i] == '=':
            print(sum_total)
        elif string[i:i+3] == "off":
            on_off = False
            i += 2
        elif string[i:i+2] == "on":
            on_off = True
            i += 1
        elif on_off:
            if string[i].isdigit():
                num = 0
                while i < len(string) and string[i].isdigit():
                    num = num * 10 + int(string[i])
                    i += 1
                sum_total += num
                continue
        i += 1

    return sum_total


# Chamando a função
print(sum_reader("Maria 01 23 4 = off 567 8 on 9"))