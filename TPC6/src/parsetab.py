
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD AP DIV FP MULT NUMBER SUB grau1  : grau2  grau1    : grau1 ADD grau2  grau1    : grau1 SUB grau2  grau2    : grau3  grau2    : grau2 MULT grau3  grau2    : grau2 DIV grau3  grau3    : NUMBER  grau3    : AP grau1 FP '
    
_lr_action_items = {'NUMBER':([0,5,6,7,8,9,],[4,4,4,4,4,4,]),'AP':([0,5,6,7,8,9,],[5,5,5,5,5,5,]),'$end':([1,2,3,4,11,12,13,14,15,],[0,-1,-4,-7,-2,-3,-5,-6,-8,]),'ADD':([1,2,3,4,10,11,12,13,14,15,],[6,-1,-4,-7,6,-2,-3,-5,-6,-8,]),'SUB':([1,2,3,4,10,11,12,13,14,15,],[7,-1,-4,-7,7,-2,-3,-5,-6,-8,]),'FP':([2,3,4,10,11,12,13,14,15,],[-1,-4,-7,15,-2,-3,-5,-6,-8,]),'MULT':([2,3,4,11,12,13,14,15,],[8,-4,-7,8,8,-5,-6,-8,]),'DIV':([2,3,4,11,12,13,14,15,],[9,-4,-7,9,9,-5,-6,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'grau1':([0,5,],[1,10,]),'grau2':([0,5,6,7,],[2,2,11,12,]),'grau3':([0,5,6,7,8,9,],[3,3,3,3,13,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> grau1","S'",1,None,None,None),
  ('grau1 -> grau2','grau1',1,'p_operacao_grau1_1','leitor_semantico.py',5),
  ('grau1 -> grau1 ADD grau2','grau1',3,'p_operacao_grau1_2','leitor_semantico.py',9),
  ('grau1 -> grau1 SUB grau2','grau1',3,'p_operacao_grau1_3','leitor_semantico.py',13),
  ('grau2 -> grau3','grau2',1,'p_operacao_grau2_1','leitor_semantico.py',19),
  ('grau2 -> grau2 MULT grau3','grau2',3,'p_operacao_grau2_2','leitor_semantico.py',23),
  ('grau2 -> grau2 DIV grau3','grau2',3,'p_operacao_grau2_3','leitor_semantico.py',27),
  ('grau3 -> NUMBER','grau3',1,'p_operacao_grau3_1','leitor_semantico.py',33),
  ('grau3 -> AP grau1 FP','grau3',3,'p_operacao_grau3_2','leitor_semantico.py',37),
]
