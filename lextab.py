# lextab.py.
_tabversion   = '3.10'
_lextokens    = set(('COLON', 'DIVIDE', 'EQUALS', 'LPAREN', 'MINUS', 'NAME', 'NUMBER_DOUBLE', 'NUMBER_INT', 'PLUS', 'RPAREN', 'TIMES'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_NUMBER_DOUBLE>\\d+\\.\\d+)|(?P<t_NUMBER_INT>\\d+)|(?P<t_newline>\\n+)|(?P<t_NAME>[a-zA-Z_][a-zA-Z0-9_]*)|(?P<t_LPAREN>\\()|(?P<t_RPAREN>\\))|(?P<t_PLUS>\\+)|(?P<t_TIMES>\\*)|(?P<t_COLON>,)|(?P<t_EQUALS>=)|(?P<t_MINUS>-)|(?P<t_DIVIDE>/)', [None, ('t_NUMBER_DOUBLE', 'NUMBER_DOUBLE'), ('t_NUMBER_INT', 'NUMBER_INT'), ('t_newline', 'newline'), (None, 'NAME'), (None, 'LPAREN'), (None, 'RPAREN'), (None, 'PLUS'), (None, 'TIMES'), (None, 'COLON'), (None, 'EQUALS'), (None, 'MINUS'), (None, 'DIVIDE')])]}
_lexstateignore = {'INITIAL': ' \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
