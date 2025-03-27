import ply.yacc as yacc
from leitor_lexico import tokens

def p_operacao_grau1_1(p):
    """ grau1  : grau2 """
    p[0] = p[1]

def p_operacao_grau1_2(p):
    """ grau1    : grau1 ADD grau2 """
    p[0] = p[1] + p[3]

def p_operacao_grau1_3(p):
    """ grau1    : grau1 SUB grau2 """
    p[0] = p[1] - p[3]



def p_operacao_grau2_1(p):
    """ grau2    : grau3 """
    p[0] = p[1]

def p_operacao_grau2_2(p):
    """ grau2    : grau2 MULT grau3 """
    p[0] = p[1] * p[3]

def p_operacao_grau2_3(p):
    """ grau2    : grau2 DIV grau3 """
    p[0] = p[1] / p[3]



def p_operacao_grau3_1(p):
    """ grau3    : NUMBER """
    p[0] = p[1]

def p_operacao_grau3_2(p):
    """ grau3    : AP grau1 FP """
    p[0] = p[2]

parser = yacc.yacc()

def main ():
    print(parser.parse("4+(1)"))

if __name__ == '__main__':
    main()