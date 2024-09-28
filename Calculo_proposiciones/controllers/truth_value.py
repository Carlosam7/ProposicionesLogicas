from tabulate import tabulate
from typing import List
import ttg

from controllers.build_tree import build_tree
from controllers.reassign import reassign
from controllers.identify_letter import identify_letter


def truth_value(proposition1: 'str', proposition2: 'str') -> bool: #Devuelve True si son equivalentes
  proposition1.lower() #Combertir todos los carácteres a mínuscula
  proposition2.lower()

  chars1: 'List' = identify_letter(proposition1) #Lista con las letras
  chars2: 'List' = identify_letter(proposition2)

  tree1 = build_tree(proposition1) #Árbol de proposiciones
  tree2 = build_tree(proposition2)

  list_prop1: 'List' = reassign(tree1.levels_nr())
  list_prop2: 'List' = reassign(tree2.levels_nr())

  table1 = ttg.Truths(chars1, reassign(list_prop1), ints=True) #Tabla de verdad
  table2 = ttg.Truths(chars2, reassign(list_prop2), ints=True)

  print(f'Tabla de de verdad: {proposition1}')
  print(tabulate(table1.as_pandas.values.tolist(), headers=table1.as_pandas.columns, tablefmt='fancy_grid'),'\n')
  print(f'Tabla de de verdad: {proposition2}')
  print(tabulate(table2.as_pandas.values.tolist(), headers=table2.as_pandas.columns, tablefmt='fancy_grid'), '\n')

  return table1.valuation() == table2.valuation() #Valor de equivalencia