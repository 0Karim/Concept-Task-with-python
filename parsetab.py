
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '529B9D6BE3A261FAD01C900950380859'
    
_lr_action_items = {'RCARL':([43,],[45,]),'ID':([5,9,16,17,],[6,14,19,19,]),'MINUS':([18,20,21,24,32,35,36,37,38,39,40,],[27,-21,-17,-20,27,-16,-15,27,-19,-18,-22,]),'PLUS':([18,20,21,24,32,35,36,37,38,39,40,],[28,-21,-17,-20,28,-16,-15,28,-19,-18,-22,]),'CASE':([8,44,],[9,9,]),'BREAK':([33,34,],[41,42,]),'DIVID':([20,21,24,35,36,38,39,40,],[-21,30,-20,30,30,-19,-18,-22,]),'SEMICOLON':([18,19,20,21,22,24,25,26,35,36,37,38,39,40,41,42,],[-12,-14,-21,-17,-11,-20,33,34,-16,-15,-13,-19,-18,-22,43,44,]),'TIMES':([20,21,24,35,36,38,39,40,],[-21,31,-20,31,31,-19,-18,-22,]),'NUMBER':([9,16,17,23,27,28,29,30,31,],[15,20,20,20,20,20,20,20,20,]),'RPAREN':([6,20,21,24,32,35,36,38,39,40,],[7,-21,-17,-20,40,-16,-15,-19,-18,-22,]),'COLON':([11,13,14,15,],[16,17,-10,-9,]),'SWITCH':([0,],[2,]),'EQUL':([19,],[29,]),'DEFAULT':([8,44,],[11,11,]),'$end':([0,1,3,4,10,12,44,45,46,],[-3,-2,-1,0,-7,-4,-5,-8,-6,]),'LPAREN':([2,16,17,23,27,28,29,30,31,],[5,23,23,23,23,23,23,23,23,]),'LCARL':([7,],[8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'var':([9,],[13,]),'empty':([0,],[1,]),'term':([16,17,23,27,28,29,],[21,21,21,35,36,21,]),'switch':([0,],[4,]),'expression':([16,17,23,29,],[18,18,32,37,]),'factor':([16,17,23,27,28,29,30,31,],[24,24,24,24,24,24,38,39,]),'switch_stmt':([0,],[3,]),'stmt_list':([16,17,],[25,26,]),'default':([8,44,],[10,10,]),'stmt':([16,17,],[22,22,]),'list_code':([8,44,],[12,46,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> switch","S'",1,None,None,None),
  ('switch -> switch_stmt','switch',1,'p_switch','Task_switch1.py',64),
  ('switch -> empty','switch',1,'p_switch','Task_switch1.py',65),
  ('empty -> <empty>','empty',0,'p_empty','Task_switch1.py',72),
  ('switch_stmt -> SWITCH LPAREN ID RPAREN LCARL list_code','switch_stmt',6,'p_switch_stmt','Task_switch1.py',78),
  ('list_code -> CASE var COLON stmt_list SEMICOLON BREAK SEMICOLON','list_code',7,'p_list_code','Task_switch1.py',83),
  ('list_code -> CASE var COLON stmt_list SEMICOLON BREAK SEMICOLON list_code','list_code',8,'p_list_code','Task_switch1.py',84),
  ('list_code -> default','list_code',1,'p_list_code','Task_switch1.py',85),
  ('default -> DEFAULT COLON stmt_list SEMICOLON BREAK SEMICOLON RCARL','default',7,'p_default','Task_switch1.py',91),
  ('var -> NUMBER','var',1,'p_var','Task_switch1.py',98),
  ('var -> ID','var',1,'p_var','Task_switch1.py',99),
  ('stmt_list -> stmt','stmt_list',1,'p_stmt_list','Task_switch1.py',105),
  ('stmt_list -> expression','stmt_list',1,'p_stmt_list','Task_switch1.py',106),
  ('stmt -> ID EQUL expression','stmt',3,'p_stmt','Task_switch1.py',112),
  ('stmt -> ID','stmt',1,'p_stmt','Task_switch1.py',113),
  ('expression -> expression PLUS term','expression',3,'p_expression','Task_switch1.py',119),
  ('expression -> expression MINUS term','expression',3,'p_expression','Task_switch1.py',120),
  ('expression -> term','expression',1,'p_expression','Task_switch1.py',121),
  ('term -> term TIMES factor','term',3,'p_term','Task_switch1.py',128),
  ('term -> term DIVID factor','term',3,'p_term','Task_switch1.py',129),
  ('term -> factor','term',1,'p_term','Task_switch1.py',130),
  ('factor -> NUMBER','factor',1,'p_factor','Task_switch1.py',137),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','Task_switch1.py',138),
]