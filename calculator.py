# Max Base
# https://github.com/BaseMax/MiniCalculatorInterpreter
import math
import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NAME',
    'NUMBER_INT', 'NUMBER_DOUBLE',
    'PLUS','MINUS','TIMES','DIVIDE',
    'EQUALS','COLON',
    'LPAREN','RPAREN',
)
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COLON   = r','
t_EQUALS  = r'='
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_ignore = ' \t'

def t_NUMBER_DOUBLE(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print('Integer value too large %d', t.value)
        t.value = 0
    return t

def t_NUMBER_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print('Integer value too large %d', t.value)
        t.value = 0
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
    
def t_error(t):
    print('Illegal character \'%s\'' % t.value[0])
    t.lexer.skip(1)

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
)
