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
