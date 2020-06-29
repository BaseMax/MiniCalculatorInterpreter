# parsetab.py
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'statementleftPLUSMINUSleftTIMESDIVIDErightUMINUSCOLON DIVIDE EQUALS LPAREN MINUS NAME NUMBER_DOUBLE NUMBER_INT PLUS RPAREN TIMES\n    statement : NAME EQUALS expression\n    \n    statement : expression\n    \n    expression : expression PLUS expression\n               | expression MINUS expression\n               | expression DIVIDE expression\n               | expression TIMES expression\n    \n    expression : MINUS expression %prec UMINUS\n    \n    expression : LPAREN expression RPAREN\n    \n    expressions : expressions COLON expression\n               | expression\n               |\n    \n    expression : NAME LPAREN expressions RPAREN\n    \n    expression : NUMBER_INT\n               | NUMBER_DOUBLE\n    \n    expression : NAME\n    '
    
_lr_action_items = {'NAME':([0,4,5,8,9,10,11,12,13,26,],[2,15,15,15,15,15,15,15,15,15,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,],[4,-15,11,4,4,-13,-14,4,4,4,4,4,4,-7,-15,11,11,11,-3,-4,-5,-6,-8,-12,4,11,]),'LPAREN':([0,2,4,5,8,9,10,11,12,13,15,26,],[5,9,5,5,5,5,5,5,5,5,9,5,]),'NUMBER_INT':([0,4,5,8,9,10,11,12,13,26,],[6,6,6,6,6,6,6,6,6,6,]),'NUMBER_DOUBLE':([0,4,5,8,9,10,11,12,13,26,],[7,7,7,7,7,7,7,7,7,7,]),'$end':([1,2,3,6,7,14,15,17,20,21,22,23,24,25,],[0,-15,-2,-13,-14,-7,-15,-1,-3,-4,-5,-6,-8,-12,]),'EQUALS':([2,],[8,]),'PLUS':([2,3,6,7,14,15,16,17,19,20,21,22,23,24,25,27,],[-15,10,-13,-14,-7,-15,10,10,10,-3,-4,-5,-6,-8,-12,10,]),'DIVIDE':([2,3,6,7,14,15,16,17,19,20,21,22,23,24,25,27,],[-15,12,-13,-14,-7,-15,12,12,12,12,12,-5,-6,-8,-12,12,]),'TIMES':([2,3,6,7,14,15,16,17,19,20,21,22,23,24,25,27,],[-15,13,-13,-14,-7,-15,13,13,13,13,13,-5,-6,-8,-12,13,]),'RPAREN':([6,7,9,14,15,16,18,19,20,21,22,23,24,25,27,],[-13,-14,-11,-7,-15,24,25,-10,-3,-4,-5,-6,-8,-12,-9,]),'COLON':([6,7,9,14,15,18,19,20,21,22,23,24,25,27,],[-13,-14,-11,-7,-15,26,-10,-3,-4,-5,-6,-8,-12,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,5,8,9,10,11,12,13,26,],[3,14,16,17,19,20,21,22,23,27,]),'expressions':([9,],[18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME EQUALS expression','statement',3,'p_statement_assign','calculator.py',62),
  ('statement -> expression','statement',1,'p_statement_expression','calculator.py',68),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','calculator.py',74),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','calculator.py',75),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','calculator.py',76),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','calculator.py',77),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','calculator.py',90),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','calculator.py',96),
  ('expressions -> expressions COLON expression','expressions',3,'p_expressions','calculator.py',102),
  ('expressions -> expression','expressions',1,'p_expressions','calculator.py',103),
  ('expressions -> <empty>','expressions',0,'p_expressions','calculator.py',104),
  ('expression -> NAME LPAREN expressions RPAREN','expression',4,'p_expression_function','calculator.py',113),
  ('expression -> NUMBER_INT','expression',1,'p_expression_number','calculator.py',162),
  ('expression -> NUMBER_DOUBLE','expression',1,'p_expression_number','calculator.py',163),
  ('expression -> NAME','expression',1,'p_expression_name','calculator.py',169),
]
